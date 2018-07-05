import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxChartsModule } from '@swimlane/ngx-charts';

import { AppComponent } from './app.component';
import { HttpModule } from '@angular/http';
import { DataService } from './services/data.service';
import { FinancePlotComponent } from './finance-plot/finance-plot.component';
import { FinanceDataService } from './services/finance-data.service';


@NgModule({
  declarations: [
    AppComponent,
    FinancePlotComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    NgxChartsModule,
    BrowserAnimationsModule,
    HttpModule 
  ],
  providers: [DataService, FinanceDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
