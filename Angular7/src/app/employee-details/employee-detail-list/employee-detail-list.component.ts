import { Component, OnInit } from '@angular/core';
import { EmployeeDetail } from 'src/app/shared/employee-detail.model';
import { EmployeeDetailService } from 'src/app/shared/employee-detail.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-employee-detail-list',
  templateUrl: './employee-detail-list.component.html',
  styles: []
})
export class EmployeeDetailListComponent implements OnInit {

  constructor(private service: EmployeeDetailService,
    private toastr: ToastrService) { }

  ngOnInit() {
    this.service.refreshList();
  }
  populateForm(pd:EmployeeDetail)
  {
    this.service.formData = Object.assign({},pd);
  }
  onDelete(ID)
  {
    if(confirm('Are you sure to delete this record ?')){
    this.service.deleteEmployeeDetail(ID)
    .subscribe(res=> {
          this.service.refreshList();
          this.toastr.warning("Deleted Successfully","Employee Details Register");
      },
      err=>
      {
        console.log(err);

      })
    }  
  }
}
