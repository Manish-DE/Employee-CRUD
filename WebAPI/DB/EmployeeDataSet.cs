using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Configuration;
using WebAPI.Model;
using System.IO;

namespace WebAPI.DB
{
    public class EmployeeDataSet
    {
        SqlConnection con;
        public EmployeeDataSet()
        {
            var configuration = GetConfiguration();
            con = new SqlConnection(configuration.GetSection("ConnectionStrings").GetSection("DevConnection").Value);
        }
        public IConfigurationRoot GetConfiguration()
        {
            var builder = new ConfigurationBuilder().SetBasePath(Directory.GetCurrentDirectory()).AddJsonFile("appsettings.json", optional: true, reloadOnChange: true);
            return builder.Build();
        }

        public IEnumerable<Employee> GetAllEmployees()
        {
            List<Employee> lstemployee = new List<Employee>();
            if (con != null && con.State == ConnectionState.Closed)
                con.Open();
            SqlCommand cmd = new SqlCommand("spGetAllEmployees", con);
            cmd.CommandType = CommandType.StoredProcedure;
            SqlDataReader rdr = cmd.ExecuteReader();
            while (rdr.Read())
            {
                Employee employee = new Employee();
                employee.ID = Convert.ToInt32(rdr["EmployeeID"]);
                employee.Name = rdr["Name"].ToString();
                employee.Gender = rdr["Gender"].ToString();
                employee.Department = rdr["Department"].ToString();
                employee.City = rdr["City"].ToString();
                lstemployee.Add(employee);
            }
            return lstemployee;
        }

        public string AddEmployee(Employee employee)
        {
            try
            {
                if (con != null && con.State == ConnectionState.Closed)
                con.Open();
                SqlCommand cmd = new SqlCommand("spAddEmployee", con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@Name", employee.Name);
                cmd.Parameters.AddWithValue("@Gender", employee.Gender);
                cmd.Parameters.AddWithValue("@Department", employee.Department);
                cmd.Parameters.AddWithValue("@City", employee.City);
                int Results = cmd.ExecuteNonQuery();
                if (Results > 0)
                   return "Saved Successfully";
                else
                   return null;
            }
            catch (Exception ex)
            {
                return "Saved Employee" + ex.Message;
            }

        }
        public string UpdateEmployee(Employee employee)
        {
            try
            {
                if (con != null && con.State == ConnectionState.Closed)
                    con.Open();
                SqlCommand cmd = new SqlCommand("spUpdateEmployee", con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@EmpId", employee.ID);
                cmd.Parameters.AddWithValue("@Name", employee.Name);
                cmd.Parameters.AddWithValue("@Gender", employee.Gender);
                cmd.Parameters.AddWithValue("@Department", employee.Department);
                cmd.Parameters.AddWithValue("@City", employee.City);
                int results = cmd.ExecuteNonQuery();
                if (results > 0)
                    return "Saved Successfully";
                else
                    return null;
            }
            catch (Exception ex)
            {
                return "Update Employee" + ex.Message; ;
            }

        }
        //Get the details of a particular employee  
        public Employee GetEmployeeData(int? id)
        {
            
            Employee employee = new Employee();
            if (con != null && con.State == ConnectionState.Closed)
                con.Open();
            string sqlQuery = "SELECT * FROM tblEmployee WHERE EmployeeID= " + id;
            SqlCommand cmd = new SqlCommand(sqlQuery, con);
            SqlDataReader rdr = cmd.ExecuteReader();
            while (rdr.Read())
            {
                employee.ID = Convert.ToInt32(rdr["EmployeeID"]);
                employee.Name = rdr["Name"].ToString();
                employee.Gender = rdr["Gender"].ToString();
                employee.Department = rdr["Department"].ToString();
                employee.City = rdr["City"].ToString();
            }
            return employee;
            
        }
        public bool DeleteEmployee(int? id)
        {
            if (con != null && con.State == ConnectionState.Closed)
                con.Open();
            SqlCommand cmd = new SqlCommand("spDeleteEmployee", con);
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.Parameters.AddWithValue("@EmpId", id);
            int Result=cmd.ExecuteNonQuery();
            if (Result > 0)
                return true;
            else
                return false;
        }

    }
}
