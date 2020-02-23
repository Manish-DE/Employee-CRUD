using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using WebAPI.DB;
using WebAPI.Model;

namespace WebAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EmployeeController : ControllerBase
    {
        EmployeeDataSet objemployee = new EmployeeDataSet();

        // GET: api/Employee
        [HttpGet]
        public IEnumerable<Employee> GetEmployee()
        {
            return objemployee.GetAllEmployees();
        }

        // GET: api/Employee/5
        [HttpGet("{id}", Name = "Get")]
        public Employee GetEmployee(int id)
        {
            return objemployee.GetEmployeeData(id);
        }

        // POST: api/Employee
        [HttpPost]
        public IActionResult PostEmployee([FromBody]Employee employee)
        {
            try
            {
                var Results = objemployee.AddEmployee(employee);
                if (Results.Length > 0)
                    return Ok();
                // return Ok(new { Result = Results });
                else
                    return BadRequest();
                //return Ok(new { Result = "Error" });
            }
            catch (Exception ex)
            {
                string message = ex.Message;
                return BadRequest();

                //return Ok(new { Result = message });
            }
        }

        // PUT: api/Employee/5
        [HttpPut("{id}")]
        public IActionResult PutEmployee(int empID,[FromBody]Employee employee)
        {
            try
            {
                if (employee.ID == empID)
                {
                    return BadRequest();
                }
                else
                {
                    string res = objemployee.UpdateEmployee(employee);
                    if (res.ToString().Length > 0)
                        return Ok(new { Result = res });
                    else
                        return BadRequest();
                }
            }
            catch (Exception ex)
            {
                string message=ex.Message;
                return Ok(new { Result = message });
            }

         //   return NoContent();
        }

        // DELETE: api/ApiWithActions/5
        [HttpDelete("{id}")]
        public IActionResult DeleteEmployee(int id)
        {
            try
            {
                bool res = objemployee.DeleteEmployee(id);
                return Ok(new { Result = res });
            }
            catch(Exception ex)
            {
                string message = ex.Message;
                return Ok(new { Result = message });
            }
        }
    }
}
