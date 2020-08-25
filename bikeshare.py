import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_input(out_message,inp_type):
   
    #checking user input.
    
    citiess=['chicago','new york city','washington']
    monthss=['january', 'february', 'march', 'april', 'may', 'june','all']
    dof_week=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    
    while True:
        user_inp=input(out_message)
        try:
            if user_inp in citiess and inp_type == 1:
                break
            elif user_inp in monthss and inp_type == 2:
                break
            elif user_inp in dof_week and inp_type == 3:
                break
            else:
                if inp_type == 1:
                    print("Sorry, your input should be: chicago , new york city or washington")
                if inp_type == 2:
                    print("Sorry, your input should be: A lattered month  or all")
                if inp_type == 3:
                    print("Sorry, your input should be: Lattered Day of the week or all")
        except ValueError:
            print("Sorry, your input is wrong")
    return user_inp

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
    city = get_input("Would you like to see the data for chicago, new york city or washington?",1)


    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_input("Which Month (all, january, ... june)?", 2)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_input("Which day? (all, monday, tuesday, ... sunday)", 3)


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
    #1-loading data into datafram
    #2-convert start time to datetime
    #3-extract required date
    #5-filtring by month 
    #6-filtering by date
    
    df = pd.read_csv(CITY_DATA[city])                     

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        
        df = df[df['month'] == month]

    
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_counted_month = df['month'].mode()[0]
    
    print('Most Popular Month:', most_counted_month)


    # TO DO: display the most common day of week
    most_counted_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Day Of Week:', most_counted_day_of_week)


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    
    print('Most Common Start Hour:', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_counted_start_station = df['Start Station'].mode()[0]
    
    print('Most Start Station:', most_counted_start_station)


    # TO DO: display most commonly used end station
    most_counted_end_station = df['End Station'].mode()[0]
    
    print('Most End Station:', most_counted_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('Total Travel Time:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('user types sats :', "\n" ,df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city != 'washington':
        
        print('gender stats: ','\n',df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        
        print('birth year stats :')
        
        most_comn_year = df['Birth Year'].mode()[0]
        
        print('Most common year:',most_comn_year)
        
        most_rcnt_year = df['Birth Year'].max()
        
        print('Most Recent year:',most_rcnt_year)
        
        earliest_year = df['Birth year'].min()
        
        print('Earliest year:',earliest_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """ the function for displaying some of rwa data the user interested in.
    
    input: DataFrame 
    output: Raw data
    """
    
    out_message=input("Do you want to see a raw data ? \n  yes/no ? ")
    start=0
    end=5
    
    while True :
        try:
            if out_message.lower() == "yes" :
                raw_dataa=df.iloc[start:end]
                print(raw_dataa)
                start +=5
                end +=5
            elif out_message.lower() == "no" :
                print("Okay")
                break
            else :
                print("Please enter a correct answer ")
                
        except ValueError:
            print("Sorry, your input is wrong it should be yes/no.")       
                
      
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
