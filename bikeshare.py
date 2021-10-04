import time
import pandas as pd
import numpy as np
import calendar
from tabulate import tabulate
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
    while True:
        city = input("Which city you would like to see it's data? chicago, new york city or washington\n")
        if city.lower() in CITY_DATA.keys():
            break
        else:
            print("Please check that you entred correct city \n")
            city = input("Which city you would like to see it's data? chicago, new york city or washington\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
          month= input("Which month would you Like to filter the data or not at all? Type \"all\" for no month filter.\n").lower()
          if month.title() in list(calendar.month_name) or month== "all":
              break
          else:
              print("Please check that you entred correct month \n")
              month= input("Which month would you Like to filter the data or not at all? Type \"all\" for no month filter.\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    while True:
         day= input("Which day would you Like to filter the data or not at all? Type \"all\" for no day filter.\n").lower()
         if day.title()  in list(calendar.day_name) or day == "all":
              break
         else:
              print("Please check that you entred correct day \n")
              day= input("Which day would you Like to filter the data or not at all? Type \"all\" for no day filter.\n")
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
        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("What is the most popular month for traveling?",popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("What is the most popular day for traveling?",popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("What is the most popular hour of the day to start your travels?",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("What is the most popular month for traveling?",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("What is the most popular End Station for traveling?",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_Start_end_station = df.groupby(['Start Station','End Station']).size().nlargest(1)

    print("What is the most popular frequent combination of start station and end station trip for traveling?\n",popular_Start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()

    # TO DO: display mean travel time
    mean_travel_time=df["Trip Duration"].mean()

    print("Calculating the next statistic...trip_duration: Total Duration:",total_travel_time, " Avg Duration:" ,mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("What is the breakdown of users?",user_types)
    if 'Gender' in df.columns:
        # Only access Gender column in this case
        # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print("What is the breakdown of gender?\n",user_gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        least_most_common = (df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0])
        print("What is the oldest, youngest, and most popular year of birth, respectively?",least_most_common)
    else:
        print('Birth Year cannot be calculated because it does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ShowData(df ,RowsCount:int,start_loc:int=0):
    """Retune specified rows from data frame
    Args:
        (Pandas dataframe) df - pandas data frame structure
        (int) RowsCount - Count of rows that you need to extract
        (int) start_loc - the position in wich the extraction begin
    Returns:
        df - Pandas DataFrame containing specified rows
    """
    return df.iloc[start_loc:RowsCount+start_loc]


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        while view_data=="yes":
                print(tabulate(ShowData(df,5,start_loc), headers ="keys"))
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
