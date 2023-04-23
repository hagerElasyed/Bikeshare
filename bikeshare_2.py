import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

          
Cities = ['chicago', 'new york city', 'washington']

Months = ['january', 'february', 'march', 'april', 'may', 'june','all']

Days = ['sunday', 'monday', 'tuesday', 'wednesday', 
        'thursday', 'friday', 'saturday','all' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ('Which city you want to explore chicago, new york city, washington?' ).lower()
        if city in Cities: 
            break
        else:
            print("invalid input! please enter valid input")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you want to choose specific month? If yes, type month name from first six months else type 'all'").lower() 
        if month in Months:
            break
        else:
            print("invalid input! please enter valid input")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want to choose specific day? If yes, type day name else 'all'").lower()
        if day in Days:
            break
        else:
            print("invalid input! please enter valid input")
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Month filter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]
    # Day filter
    if day != 'all':        
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month    
    common_month =  df['month'].mode()[0] 
    print('Most common month is: ', common_month)
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is: ', common_day)
    # display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    common_hour = df['start hour'].mode()[0]
    print('Most common hour is: ', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station is: ', common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station is: ', common_end_station)
    # display most frequent combination of start station and end station trip
    df['trip'] =  df['Start Station'] +' to: '+ df['End Station']
    common_trip = df['trip'].mode()[0]
    print('Most common trip is from: ', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in hours is: ', total_travel_time/3600)
    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time in minutes is: ', avg_travel_time/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usertype_counts = df['User Type'].value_counts()
    print('counts of user types are: ', usertype_counts)

    # Display counts of gender
    
    try:
        
        gender_counts = df['Gender'].value_counts()
        print('counts of gender are: ', gender_counts)
    
        # Display earliest, most recent, and most common year of birth
        earliest_birthyear = df['Birth Year'].min()
        recent_birthyear = df['Birth Year'].max()
        common_birthyear = df['Birth Year'].mode()[0]
        print('birth year for oldest user is {} and youngest user is {} while the most common birth year is {}'.format(int(earliest_birthyear), int(recent_birthyear), int(common_birthyear)))
    except:
        print('')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to perview only five raws data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x + 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
