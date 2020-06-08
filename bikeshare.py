#Imporing all the major files required in the analysis of bikeshare problem
#Importing time,pandas,stastics,math
import time
import datetime
import pandas as pd
import statistics as st
import math


# Using Dictionary city_names  with key washington,chicago,new york with their .csv data  respectively
CITY_NAMES = { 'washington': 'washington.csv',
              'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
             }

def get_information():
    # This function request the user to input the information for seacrching and analyzing the bikeshare data ,according to inputs given data processed acordingly
   # Asks the [erson] to specify the city, month, and day to analyze.


     # asks  user  to input for city (chicago, new york city, washington). 
    print("Ciao!, Let's explore some United Nation  bikeshare data today!")
  
    # user enter the  city name for which they need data
    city_value = input("\nFrom which city today you wanted to see the data ,list of available cities are  NEW YORK , CHICAGO , WASHINGTON/n \n")
    #since user can enter the value of city in lower or upper case so we have to convert it in lower form to proceed forward
    city_value.lower()
   
    #Here we are using while loop to check whether appropriate data is entered by our user or not ,if appropriate data is not entered a message will be popped out to the user to enter the data again
    
    while(True):
        if(city_value == 'new york' or city_value == 'chicago' or city_value == 'washington' or city_value == 'all'):
            break
        else:
            city_value = input("/nPlease Enter The  Correct city*please see the upper list for valid city: \n")
            city_value.lower()
      
    #  user input for month for which they want to see the data available one's are (January, February, March, April, May, or June) 
    month_value = input(""""\nEnter which month? January, February, March, April, May, or June?, \n""")
    month_value.lower()
    
   # here checking again whether the entered month by the user is valid or not,if it's not valid ,promppt the message to enter it again
    while(True):
        if(month_value == 'january' or month_value == 'february' or month_value == 'march' or month_value == 'april' or month_value == 'may' or month_value == 'june' or month_value == 'all'):
            break
        else:
            month = input('Please enter  the valid month* for details please see above\n')
            month_value.lower()            
    # enter user input for day of week ( monday, tuesday,wednesday ... sunday) or choose all to display the data for all 7 days of week
    day_value =  input('Which day  monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n')
    day_value.lower()
    while(True):
        
        if(day_value == 'monday' or day_value == 'tuesday' or day_value == 'wednesday' or day_value == 'thursday' or day_value == 'friday' or day_value == 'saturday' or day_value == 'sunday' or day_value == 'all'):
            break
        else:
            day_value = input('Please enter  the Correct day: ')
            day_value.lower()
            


    print("All Data Successfully Recorded")
    print('-'*100)
          
    return city_value, month_value, day_value

def calculate_data(city, month, day):

   # Loads data for the specified city and filters by month and day if applicable.
    
    #df - Pandas DataFrame containing city value filtered by month and day is used
    
    cd = pd.read_csv(CITY_NAMES[city])

 
    cd['Start Time'] = pd.to_datetime(cd['Start Time'])
    # Datetime is used to convert date into date format
    cd['End Time'] = pd.to_datetime(cd['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #we need to find the index of the month
        month = months.index(month) + 1       

        cd = cd[cd['Start Time'].dt.month == month]
        
    #filter data by day.
    if day != 'all': 
        cd = cd[cd['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(cd.head())
    return cd


def stats_of_time(cd, month, day):
    #Displays statistics on the most frequent times of travel

    print('\nNow Calculating The Most Frequent Times of Travel.........\n')
    start_time = time.time()

    # display the most common month
    if(month == 'all'):
        most_common_month = cd['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # display the most common day of week
    if(day == 'all'):
        most_common_day = cd['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # display the most common start hour
    most_common_hour = cd['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    


def stats_of_station(cd):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = st.mode(cd['Start Station'])
    print('\nMost common start station is {}\n'.format(most_common_start_station))

    # It display most commonly used end stations
    most_common_end_station = st.mode(cd['End Station'])
    print('\nMost common end station is {}\n'.format(most_common_end_station))

    # It display most frequent combination of start station and end station trip
    combination_trip = cd['Start Station'].astype(str) + " to " + cd['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    


def stats_trip_duration_(ds):
    #It Displays the stastics average or total duration

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays the  total travel time 
    total_travel_time = ds['Trip Duration'].sum()
    first_time = total_travel_time
    day = first_time // (24 * 3600)
    first_time = first_time % (24 * 3600)
    hour = first_time // 3600
    first_time %= 3600
    minutes = first_time // 60
    first_time %= 60
    seconds = first_time
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # Here it displays mean travel time
    mean_travel_time = ds['Trip Duration'].mean()
    second_time = mean_travel_time
    second_day = second_time // (24 * 3600)
    second_time = second_time % (24 * 3600)
    second_hour = second_time // 3600
    second_time %= 3600
    second_minute = second_time // 60
    second_time %= 60
    seconds2 = second_time
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(second_hour, second_minute, seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))


def stats_user(us1):
    #To display the stastics of bikeshare data

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    no_of_subscribers = us1['User Type'].str.count('Subscriber').sum()
    no_of_customers = us1['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('\nNumber of customers are {}\n'.format(int(no_of_customers)))

    # Display counts of gender
    if('Gender' in us1):
        male_count = us1['Gender'].str.count('Male').sum()
        female_count = us1['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))


    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in us1):
        earliest_year = us1['Birth Year'].min()
        recent_year = us1['Birth Year'].max()
        most_common_birth_year = st.mode(us1['Birth Year'])
        print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    


def main():
    while True:
        city, month, day = get_information()
        cd = calculate_data(city, month, day)

        stats_of_time(cd, month, day)
        stats_of_station(cd)
        stats_trip_duration_(cd)
        stats_user(cd)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()