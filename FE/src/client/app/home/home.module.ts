import { NgModule } from '@angular/core';
import { HomeComponent } from './home.component';
import { HomeRoutingModule } from './home-routing.module';
import { SharedModule } from '../shared/shared.module';
import { AlertModule } from 'ng2-bootstrap/alert';
import { DropdownModule } from 'ng2-bootstrap/dropdown';
import { TabsModule } from 'ng2-bootstrap/tabs';

@NgModule({
  imports: [HomeRoutingModule, SharedModule,  AlertModule.forRoot(), DropdownModule.forRoot(), 
    TabsModule.forRoot()],
  declarations: [HomeComponent],
  exports: [HomeComponent],
  providers: []
})
export class HomeModule { }
