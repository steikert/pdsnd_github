import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        """
        converts input to lower cases and checks if input in defined list
        """
        city = input('Please choose Chicago, New York City, or Washington: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month = ''
    while month not in months:
        month = input('Be so kind and select a particular month of a year or all to analyze the entire year: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in days:
        day = input('Please choose a day of the week or all to analyze the entire week: ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loading data
    filename    = str(city).replace(' ', '_') + '.csv'
    df          = pd.read_csv(filename)

    # change to date format
    df['Start Time']    = pd.to_datetime(df['Start Time'])
    df['Month']         = df['Start Time'].dt.month_name()
    df['Month']         = df['Month'].str.lower()

    df['Weekday']       = df['Start Time'].dt.weekday_name
    df['Weekday']       = df['Weekday'].str.lower()

    #filtering data set
    if month != 'all':
        df    = df[df.Month == month]

    if day  != 'all':
        df   = df[df.Weekday == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        (dataframe) df - data frame to analyze"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode().iloc[0]
    print('Common month: ', common_month)

    # TO DO: display the most common day of week
    common_weekday = df['Weekday'].mode().iloc[0]
    print('Common weekday: ', common_weekday)

    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode().iloc[0]
    print('Common start hour: ', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        (dataframe) df - data frame to analyze"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_loc = df['Start Station'].mode().iloc[0]
    print('Common start station: ', common_start_loc)

    # TO DO: display most commonly used end station
    common_end_loc = df['End Station'].mode().iloc[0]
    print('Common end station: ', common_end_loc)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combined'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    common_start_end = df['start_end_combined'].mode().iloc[0]
    print('Common start & end station: ', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        (dataframe) df - data frame to analyze"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time: ', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time: ', mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

    Args:
        (dataframe) df - data frame to analyze"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df.groupby('User Type')['User Type'].nunique()
    print('Count by user type: ', count_user_types, '\n')

    try:
        # TO DO: Display counts of gender
        count_gender = df.groupby('Gender')['Gender'].nunique()
        print('Count by gender: ', count_gender, '\n')
    except:
        print('Gender data is not available in this data set.\n')

    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_dob = df['Birth Year'].min().astype('int')
        print('Earliest date of birth: ', earliest_dob, '\n')

        recent_dob = df['Birth Year'].max().astype('int')
        print('Recent date of birth: ', recent_dob, '\n')


        common_dob  = df['Birth Year'].mode().iloc[0].astype('int')
        print('Common date of birth: ', common_dob, '\n')
    except:
        print('DoB data is not available in this data set.\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """Displays raw data used for the analysis.

     Args:
        (dataframe) df - data frame to analyze"""

    tmp= input('If you want to see the raw data used for the analysis then please type yes or anything else for no: ').lower()

    index = 0
    while tmp == 'yes':
        print(df[index:index+5],'\n')
        tmp     = input('Do you want to see the next 5 rows: ').lower()
        index   += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
