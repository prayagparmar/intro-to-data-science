__author__ = 'prayagparmar'
from pandas import DataFrame, Series
import numpy


def create_dataframe():
    '''
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the  table of 2014 Sochi winter olympics medal counts.

    The columns for this dataframe should be called
    'country_name', 'gold', 'silver', and 'bronze'.

    There is no need to  specify row indexes for this dataframe
    (in this case, the rows will  automatically be assigned numbered indexes).

    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]


    # your code here

    data = {'country_name': Series(countries), 'gold': Series(gold), 'silver': Series(silver),
            'bronze': Series(bronze)}

    olympic_medal_counts_df = DataFrame(data)

    return olympic_medal_counts_df


def average_bronze_count_at_least_one_gold():
    '''

    Compute the average number of bronze medals earned by countries who
    earned at least one gold medal.

    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.

    '''

    df = create_dataframe()

    return numpy.mean(df['bronze'][df['gold'] >= 1])


def avg_medal_count():
    '''
    Using the dataframe's apply method, create a new Series called
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at
    least one medal of any kind at the 2014 Sochi olympics.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    df = create_dataframe()

    # YOUR CODE HERE
    # applymap is used when the method needs to be applied to all the series' in the dataframe
    return df[['bronze', 'silver', 'gold']].apply(numpy.mean)


def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    # Alternate solution using only pandas

    # df['points'] = df[['gold','silver','bronze']].dot([4, 2, 1])
    # olympic_points_df = df[['country_name','points']]

    # YOUR CODE HERE
    df = create_dataframe()

    df['points'] = numpy.dot(df[['bronze', 'silver', 'gold']], [1, 2, 4])
    return df[['country_name', 'points']]


if __name__ == "__main__":
    print(average_bronze_count_at_least_one_gold())
    print(avg_medal_count())
    print(numpy_dot())