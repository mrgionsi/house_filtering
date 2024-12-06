import { Component, OnInit } from '@angular/core';
import { TableModule } from 'primeng/table'; // Import the TableModule
import { ItemDataService } from '../services/item-data.service';
import { Item } from '../models/item.model';
import { NumberFormatPipe } from '../number-format.pipe';
import { CommonModule } from '@angular/common';
import { RatingModule } from 'primeng/rating';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-house-results',
  standalone: true,
  imports: [TableModule, CommonModule, NumberFormatPipe, RatingModule, FormsModule],
  templateUrl: './house-results.component.html',
  styleUrl: './house-results.component.scss'
})
export class HouseResultsComponent implements OnInit {
  data: Item[] = [];

  constructor(private dataService: ItemDataService) { } // Inject DataService
  ngOnInit(): void {
    this.loadData();
  }

  toggleSaved(itemId: number, saved: boolean): void {
    // Call the API service to update the 'saved' state of the item
    this.dataService.toggleSaved(itemId, !saved).subscribe(
      response => {
        console.log('Item updated:', response);
        // Optionally, update the local item data
        const item = this.data.find(i => i.id === itemId);
        if (item) {
          item.saved = !saved;  // Toggle the saved state locally
        }
      },
      error => {
        console.error('Error updating item:', error);
      }
    );
  }

  setClicked(id: number): void {
    console.log("clicked");

    this.dataService.setClicked(id).subscribe({
      next: (data) => {
        // Check if the response is successful (status code 200)
        console.log(data)

        console.log(data.status)
        if (data && data.status === 200) { // Adjust this condition based on your actual response structure
          // Assuming 'item' is accessible here and has a 'clicked' property
          // You might need to find the item based on the id if it's not in the current context
          const item = this.data.find(item => item.id === id);
          if (item) {
            item.clicked = true; // Update the clicked property
            // Create a new reference to trigger change detection
            this.data = [...this.data]; // This line ensures that Angular detects the change
          }
          console.log('Data set: ', data);
        } else {
          console.error('Unexpected response: ', data);
        }
      },
      error: (err) => {
        console.error('Error loading data: ', err);
      },
      complete: () => {
        console.log('Data loading completed');
      }
    });
  }

  // Handle rating change when the user clicks the stars
  onRatingChange(item: any) {
    console.log(`Item with ID ${item.id} rated as: ${item.rating}`);
    var rating = item.rating;
    this.dataService.changeRating(item.id, item.rating).subscribe(
      response => {
        console.log('Item updated:', response);
        // Optionally, update the local item data
        const item2: any = this.data.find(i => i.id === item.id);
        if (item2) {
          item2.rating = rating;  // Toggle the saved state locally
        }
      },
      error => {
        console.error('Error updating item:', error);
      }
    );

  }

  loadData(): void {
    this.dataService.getData().subscribe({
      next: data => {
        this.data = data;
        //console.log('Data loaded: ', data)
      },
      error: err => console.error('Error loading data: ', err),
      complete: () => console.log('Data loading completed')
    });
  }

  parseFormattedValue(value: string): number {
    // Remove any non-numeric characters except commas or periods
    value = value.replace(/[^\d,\.]/g, ''); // Remove currency symbols or non-numeric characters

    // Remove thousands separators (periods or commas)
    value = value.replace(/\./g, '').replace(/,/g, '');

    // Convert the resulting string to an integer
    return value ? parseInt(value, 10) : 0;
  }
  customSort(event: any) {
    const field = event.field;
    const order = event.order;

    // Function to parse formatted values (if needed for other columns)
    const parseFormattedValue = (value: string): number => {
      if (!value || value.toLowerCase() === 'prezzo su richiesta') {
        return Number.MAX_SAFE_INTEGER; // Treat as highest for sorting
      }

      // Remove currency symbols and handle locale-specific separators
      value = value.replace(/[^\d,.-]/g, ''); // Remove non-numeric, non-separator characters
      value = value.replace('.', '').replace(',', '.'); // Convert to standard decimal format

      return parseFloat(value) || 0;
    };

    // Sort data array
    this.data.sort((data1: any, data2: any) => {
      let value1;
      let value2;

      // Use 'price' when sorting 'formattedValue'
      if (field === 'formattedValue') {
        value1 = data1['price'];
        value2 = data2['price'];
      } else {
        // Use the raw field value for other columns
        value1 = data1[field];
        value2 = data2[field];

        // Parse formatted values if required
        if (field === 'formattedValue') {
          value1 = parseFormattedValue(value1);
          value2 = parseFormattedValue(value2);
        }
      }

      // Compare values
      if (value1 > value2) return order;
      if (value1 < value2) return -order;
      return 0;
    });
  }



}
