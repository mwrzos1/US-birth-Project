
#read the CSV file and split the string on the newline

file = open("US_births_1994-2003_CDC_NCHS.csv","r")
o = file.read()
line_list= o.split("\n")
(line_list[0:10])

# function that reads file with no header, splits each row on the comma delimeter

def read_csv(filename):
    f = open(filename,"r")
    d = f.read()
    string_list = d.split("\n")[1:len(d)]
    final_list =[]
    for row in string_list:
        int_fields =[]
        string_fields = row.split(",")
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]
    
#function that calculates number of births in US each month

def month_births(list_lists):
    births_per_month ={}
    for index in list_lists:
        month= index[1]
        births = index[4]
        if month in births_per_month:
            births_per_month[month]= births_per_month[month]+ births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_month_births = month_births(cdc_list)
cdc_month_births
            
#function that calculates number of births per each day of week
			
def dow_births(list_lists):
    births_per_day = {}
    for data in list_lists:
        day_of_week = data[3]
        births = data[4]
        if day_of_week in births_per_day:
            births_per_day[day_of_week]=births_per_day[day_of_week] + births
        else:
            births_per_day[day_of_week] = births
    return births_per_day

cdc_day_births = dow_births(cdc_list)
cdc_day_births

#function that calculates yearly total of births

def  calc_counts(data,column):
    total_column = {}
    for index in data:
        column_value = index[column]
        births = index[4]
        if column_value in total_column:
            total_column[column_value] = total_column[column_value]+ births
        else:
            total_column[column_value] = births
    return total_column

cdc_year_births=calc_counts(cdc_list,0)
cdc_year_births


#function that calculates monthly total of births

cdc_month_births = calc_counts(cdc_list,1)
cdc_month_births


#function that calculates day of the month total

cdc_dom_births = calc_counts(cdc_list,2)
cdc_dom_births


# function that calculates day of the week total


cdc_dow_births = calc_counts(cdc_list,3)
cdc_dow_births

