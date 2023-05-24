import pandas as pd from sqlalchemy 
import create_engine,text
user = 'root'  # user name
pw = 'root'  # password
db = 'test_db'  # database name create before run
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")#connection
sal= pd.read_csv(r"C:\Users\LENOVO\Downloads\Salaries.csv")#use native location of your desktop
emp=pd.read_csv(r"C:\Users\LENOVO\Downloads\Employees.csv")#use native location of your desktop
dept=pd.read_csv(r"C:\Users\LENOVO\Downloads\Departments.csv")#use native location of your desktop
dept.to_sql('departments', con = engine, if_exists = 'replace', chunksize = 1000, index = False)
emp.to_sql('employees', con = engine, if_exists = 'replace', chunksize = 1000, index = False)
sal.to_sql('salaries', con = engine, if_exists = 'replace', chunksize = 1000, index = False)
sql = 'select monthdata.name as DEPT_NAME,round(avg(sup),0) as `AVG_MONTHLY_SALARY (USD)` from (select d.name,s.`month (yyyymm)`,(sum(`amt (usd)`)) sup from departments d inner join employees e on d.id=e.`dept id` inner join salaries s on e.id=s.emp_id group by d.name,s.`month (yyyymm)`) monthdata group by monthdata.name;'
df = pd.read_sql_query(sql=text(sql), con=engine.connect())
df.to_csv('Output.csv', encoding = 'utf-8',index=False)#creating new csv file