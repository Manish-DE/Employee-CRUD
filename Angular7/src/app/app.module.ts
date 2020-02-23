import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from "@angular/common/http";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { ToastrModule } from 'ngx-toastr';

import { AppComponent } from './app.component';
import { EmployeeDetailsComponent } from './employee-details/employee-details.component';
import { EmployeeDetailComponent } from './Employee-details/employee-detail/employee-detail.component';
import { EmployeeDetailListComponent } from './Employee-details/employee-detail-list/employee-detail-list.component';
import { EmployeeDetailService } from './shared/employee-detail.service';




@NgModule({
  declarations: [
    AppComponent,
    EmployeeDetailsComponent,
    EmployeeDetailComponent,
    EmployeeDetailListComponent
    

  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule, 
    ToastrModule.forRoot()
  ],
  providers: [EmployeeDetailService],
  bootstrap: [AppComponent]
})
export class AppModule { }
