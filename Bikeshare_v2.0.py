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
    
    
    while True:
        city_input = input("\n Select the name for which you want to explore data Chicago,Washington,New York City \n").lower()
        if city_input not in CITY_DATA:
            print("Given Input is Incorrect only selection is valid from the given list")
            continue
        else:
            city = city_input
            break 

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_list = ['All','January','February','March','April','May','June']

    while True:
        month_input = input("\n Enter the month name for which you want to explore data of January,February,March,April,May,June \n").title()
        if month_input not in month_list:
            print("Given input is incorrect kindly correct it to proceed further")
            continue
        else:
            month = month_input
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    week_day_list = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    while True:
        week_day_input = input("\n Enter the week day name for which you want to explore data \n").title()
        if week_day_input not in week_day_list:
            print("Given input incorrect kindly correct it to proceed further")
            continue
        else:
            day = week_day_input
            break


    print('-'*40)
    return city, month,day

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
    # load data file into a dataframe
    df = pd.read_csv('C:\\Users\\S.Jhunjhunwala2\\OneDrive - Shell\\Documents\\Learning\\Nano Degree\\Python Bikeshre Project\\' + CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #print(df['day_of_week'])


    # filter by month if applicable
    if month != 'All':
         #use the index of the months list to get the corresponding int
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            month = months.index(month) + 1
    
        # filter by month to create the new dataframe
            df = df[df['month'] == month ]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)
    print("Most Common month is {}".format(common_month))


    # TO DO: display the most common day of week
    common_week_day = df['day_of_week'].mode()[0]
    print("Most Common week day is {}".format(common_week_day))


    # TO DO: display the most common start hour
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    common_start_hour = df['Hour'].mode()[0]
    print("Most Common Hour of Travel Start Time is {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Commonly used start station is {}".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("Most Commonly used End station is {}".format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip

    print("Most frequent combination of start station and end station trip is {}".format((df['Start Station'] + ':' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['Time Difference'] = (df['End Time'] -df['Start Time']).dt.total_seconds()
    total_time = df['Time Difference'].sum(axis =0)
    print("Total travel time in hours {}".format(round(total_time/3600),5))
    # total_time = df['Time Difference'].sum(axis =0)
    # days, hours, minutes,second = total_time.days * 24, total_time.seconds // 3600, total_time.seconds % 3600 / 60.0
    # print("Total travel time in hrs is {}".format(days + hours + second))


    # TO DO: display mean travel time
    time_mean = df['Time Difference'].mean()
    print("Mean travel time in minutes {}".format(round(time_mean/60),5))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Type_names = df['User Type'].value_counts(ascending=True).index
    User_Type_Count = df['User Type'].value_counts(ascending=True)
    for i in range(len(User_Type_names)):
        # count_usertype = User_Type_Count[User_Type_names[i]]
        print("User Type Count for the {} is {}".format(User_Type_names[i],User_Type_Count[User_Type_names[i]]))

    # TO DO: Display counts of gender

    if 'Gender' in df:
        Gender_Type_names = df['Gender'].value_counts(ascending=True).index
        Gender_Count = df['Gender'].value_counts(ascending=True)
        for i in range(len(Gender_Type_names)):
            print("Count for the {} is {}".format(Gender_Type_names[i],Gender_Count[Gender_Type_names[i]]))
    else:
        print("Gender data is not available")

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        print("Earliest Year Of Birth Is {}".format(df['Birth Year'].min()))
        print("Most Recent Year Of Birth Is {}".format(df['Birth Year'].max()))
        print("Common Year Of Birth Is {}".format(df['Birth Year'].mode()[0]))
    else:
        print("Birth Year Data Is Not Available")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print(df.iloc[range(0,5)])
        
        
        while True:
            raw_data_visualize = input("\n Do you want to see more RAW data? Enter yes or no.\n")
            if raw_data_visualize != 'no':
                i=5                    
                print(df.iloc[range((i),(i)+5)])
                (i)+=5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()