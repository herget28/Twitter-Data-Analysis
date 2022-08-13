import streamlit as st 
import sqlite3

con = sqlite3.connect('sqlite.db')
cur = con.cursor()

city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']


cur.execute('create table if not exists teableOne (id int, date text, full_name text, country text, age int, contact text)')
cur.execute("insert into teableOne values (1, '12-08-2022', 'Hermela Getnet 1', 'Ethiopia', 23, 'hermelagetnet90@gmail.com')")
cur.execute("insert into teableOne values (2, '12-08-2022', 'Hermela Getnet 2', 'Ethiopia', 23, 'hermelagetnet90@gmail.com')")
cur.execute("insert into teableOne values (3, '12-08-2022', 'Hermela Getnet 3', 'Ethiopia', 23, 'hermelagetnet90@gmail.com')")
cur.execute("insert into teableOne values (4, '12-08-2022', 'Hermela Getnet 4', 'Ethiopia', 24, 'hermelagetnet90@gmail.com')")
cur.execute("insert into teableOne values (5, '12-08-2022', 'Hermela Getnet 5', 'Ethiopia', 24, 'hermelagetnet90@gmail.com')")

cur.execute("update teableOne set full_name = 'Hermela Getnet Updated' where id = 2")


def get_table_data(query):
	table_data = cur.execute(query).fetchall()
	for row in table_data:
		st.info(row)


def main():
	st.title("10 Academy Batch6")

	menu = ["Page One", "Page Two"]
	choice = st.sidebar.selectbox("Hermela Getnet", menu)

	if choice == "Page One":
		st.subheader("Day 6, Task 4")

		with st.form(key='query_form'):
			raw_code = st.text_area("SQL Code Here")
			submit_code = st.form_submit_button("Execute")

		with st.expander("Table One Result"):
			get_table_data('select * from tableOne')

	else:
		st.subheader("About")


if __name__ == '__main__':
	main()