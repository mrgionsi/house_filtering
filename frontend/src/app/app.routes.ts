import { Routes } from '@angular/router';
import { HouseResultsComponent } from './house-results/house-results.component';
import { SearchComponent } from './search/search.component';

export const routes: Routes = [
    { path: '', component: HouseResultsComponent },  // Default route
    { path: 'search', component: SearchComponent },  // Default route

];