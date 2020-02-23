import { Injectable } from '@angular/core';
import { EmployeeDetail } from './employee-detail.model';
import { HttpClient } from "@angular/common/http"

@Injectable({
  providedIn: 'root'
})
export class EmployeeDetailService {
  formData:EmployeeDetail
  readonly rootURL = 'http://localhost:62105/api';
  list : EmployeeDetail[];

  constructor(private http:HttpClient) { }
  PostEmployeeDetail() { 
    return this.http.post(this.rootURL + '/Employee', this.formData);
  }
  PutEmployeeDetail() { 
    return this.http.put(this.rootURL + '/Employee/'+ this.formData.ID, this.formData);
  }
  deleteEmployeeDetail(id) { 
    return this.http.delete(this.rootURL + '/Employee/'+ id);
  }
  
  refreshList(){
    this.http.get(this.rootURL + '/Employee')
    .toPromise()
    .then(res => this.list = res as EmployeeDetail[]);
  }

}
