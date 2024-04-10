# IPL Analysis

import pandas as pd # type: ignore

# 1. Data Preparation
def load_data():
    points_table = pd.read_csv('IPL \'24 Predictions - Points Table.csv')
    results = pd.read_csv('IPL \'24 Predictions - Results.csv')
    fixtures = pd.read_csv('IPL \'24 Predictions - Fixtures.csv')
    return points_table, results, fixtures

def calculate_ratio(column):
    ratios = []
    for row in column:
        runs, overs = map(float, row.split('/'))
        total_balls = int(overs) * 6 + (overs - int(overs)) * 10
        ratio = runs / total_balls
        ratios.append(ratio)
    return ratios

def load_venue_data():
    venues = {
        "RAJASTHAN ROYALS": "Sawai Mansingh Stadium, Jaipur",
        'KOLKATA KNIGHT RIDERS': 'Eden Gardens, Kolkata',
        'LUCKNOW SUPER GIANTS': 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
        'CHENNAI SUPER KINGS': 'MA Chidambaram Stadium, Chennai',
        'SUNRISERS HYDERABAD': 'Rajiv Gandhi International Stadium, Hyderabad',
        'PUNJAB KINGS': 'PCA New Stadium, Mullanpur',
        'GUJARAT TITANS': 'Narendra Modi Stadium, Ahmedabad',
        'MUMBAI INDIANS': 'Wankhede Stadium, Mumbai',
        'ROYAL CHALLENGERS BENGALURU': 'M Chinnaswamy Stadium, Bengaluru',
        'DELHI CAPITALS': 'Arun Jaitley Stadium, Delhi',
    }
    return venues

def prepare_data(points_table):
    points_table['For Ratio'] = calculate_ratio(points_table['FOR'])
    points_table['Against Ratio'] = calculate_ratio(points_table['AGAINST'])
    points_table['Difference'] = points_table['For Ratio'] - points_table['Against Ratio']
    venues = load_venue_data()
    team_info = points_table[['TEAM', 'Difference']].set_index('TEAM')
    team_info['Home'] = team_info.index.map(venues)  # Assign home venues based on team name
    return team_info

# 2. Algorithm Selection
#  1. If both teams have a positive difference between For versus Against ratio, favor the home team to win. If venue is neutral, favor the team with greater difference to win.
#  2. If both teams have a negative difference between For versus Against ratio, favor the home team to win. If venue is neutral, favor the team with lesser difference to win.
#  3. If one team has a negative For versus Against ratio, and the other team has a positive For versus Against ratio, favor the team with the positive difference. 
#  4. Ignore the matches with TBD in the fixtures
def predict_winner(row, team_info):
    team1, team2, venue = row['Team 1'], row['Team 2'], row['Venue']
    team1_diff, team2_diff = team_info.loc[team1, 'Difference'], team_info.loc[team2, 'Difference']
    if (team1_diff > 0 and team2_diff > 0) or (team1_diff < 0 and team2_diff < 0):
        if venue == team_info.loc[team1, 'Home']:
            return team1
        elif venue == team_info.loc[team2, 'Home']:
            return team2
        else:
            return team1 if abs(team1_diff) > abs(team2_diff) else team2
    else:
        return team1 if team1_diff > team2_diff else team2

# 3. Loading Input and Generating Output
def generate_predictions(fixtures, team_info):
    filtered_fixtures = fixtures[~fixtures['Team 1'].str.contains('TBD') & ~fixtures['Team 2'].str.contains('TBD')]
    filtered_fixtures['Predicted Winner'] = filtered_fixtures.apply(lambda row: predict_winner(row, team_info), axis=1)
    return filtered_fixtures[['Match', 'Venue', 'Team 1', 'Team 2', 'Predicted Winner']]

def update_points_table(predictions, points_table):
    if 'Predicted PTS' not in points_table.columns:
        points_table['Predicted PTS'] = points_table['PTS'].copy()
    for winner in predictions['Predicted Winner']:
        points_table.loc[points_table['TEAM'] == winner, 'Predicted PTS'] += 2
    return points_table.sort_values(by=['Predicted PTS', 'NRR'], ascending=False).reset_index(drop=True)

def main():
    points_table, results, fixtures = load_data()
    team_info = prepare_data(points_table)
    predictions = generate_predictions(fixtures, team_info)
    updated_points_table = update_points_table(predictions, points_table)
    print("Predictions:\n", predictions.to_string(index=False

))
    print("\nUpdated Points Table:\n", updated_points_table[['TEAM', 'Predicted PTS', 'NRR']].to_string(index=False))

if __name__ == "__main__":
    main()
