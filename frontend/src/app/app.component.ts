import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { MenuItem } from 'primeng/api';
import { MenuModule } from 'primeng/menu';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MenuModule, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  items: MenuItem[] | undefined;


  title = 'House Filtering';
  constructor(private router: Router) { }

  ngOnInit() {
    this.items = [
      {
        label: 'Navigate',
        items: [
          {
            label: 'Home',
            icon: 'pi pi-palette',
            route: '/'
          },
          {
            label: 'Search',
            icon: 'pi pi-link',
            route: '/search'
          },
          {
            label: 'Settings',
            icon: 'pi pi-cog',
            route: '/settings'
          }

        ]
      }
    ];
  }
}