# Business Fundementals: Shanghai Expat Rental Market

## Question/Need:
*What is the framing question of your analysis, or the purpose of the model/system you plan to build?*  
The Shanghai rental market is saturated with "second landlords"/property mangement companies who sign a long lease with a property owner, invest money to renovate the property, and rent out that property to foreigners at a higher rate. These landlords rely on their rental units to be occupied with very little vacancy time to minimize loss and maximize income. Each day the property does not have a tenant is a day they are paying rent to the property owner and not making income. They also need to recover their loss from the initial investment they made to renovate the space.  

To my knowledge, there has been no analysis done on pricing, amenities, location, and saturation, which would help determine if a property is a worthy investment.

*Who benefits from exploring this question or building this model/system?*  
This data aggregation would be used to help a Chinese property management company make informed decisions about investing in rental listings and executing rennovations.


## Data Description:  
*What dataset(s) do you plan to use, and how will you obtain the data?*  
I plan to scrape data from [JiaZaiShanghai](http://jiazaishanghai.com/), a popular open source listing hub for "second landlords"/property managers to advertising their listings as well as [Smart Shanghai](https://www.smartshanghai.com/housing/apartments-rent/).  

I have also found some [Shanghai foreign population data](http://tjj.sh.gov.cn/tjnj/nj19.htm?d1=2019tjnj/C0211.htm), which lists the population of foreigners by region across a few different years from 2005 - 2018.  

I am also hopefully to find a data which includes foreign companies in Shanghai and their addresses to accompany the other two data sets.  

## Tools:  
*How do you intend to meet the tools requirement of the project?*  
- I will perform exploratory data analysis in Google Sheets and data visualization in Tableau  

*Are you planning in advance to need or use additional tools beyond those required?*  
- No, not at the moment.  


## MVP Goal:  
*What would a minimum viable product (MVP) look like for this project?*  
- Data fully scraped from two websites and organized into a database
- Data cleaned (missing values, bad formatting, check duplicates)
- List addresses to be mapped out in Tableau
- Visualize foreign population data in Shanghai
