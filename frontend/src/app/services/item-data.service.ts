import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { Item } from '../models/item.model'; // Adjust the path as necessary
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ItemDataService {
  private apiUrl = environment.backend_url; // Correctly formatted URL

  constructor(private http: HttpClient) { }

  setClicked(id: number): Observable<any> {
    console.log("in the method")
    return this.http.patch(this.apiUrl + '/set-clicked', { id: id }, {
      headers: {
        'Content-Type': 'application/json',
      }
    }).pipe(
      catchError((error: any) => {
        console.error('Error in setClicked:', error);
        return throwError(() => new Error('Failed to update clicked status')); // Updated usage
      })
    );
  }

  getData(): Observable<Item[]> {
    return this.http.get<Item[]>(this.apiUrl + '/get-data', {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      })
    }).pipe(
      catchError((error: any) => {
        console.error('Error in getItems:', error);
        return throwError(() => new Error('Failed to fetch data'));
      })
    );
  }

  // Method to toggle the 'saved' state of an item
  toggleSaved(itemId: number, savedValue: boolean): Observable<any> {
    const url = `${this.apiUrl}/api/item/${itemId}/save`;  // Build the API URL with the item ID
    const body = { saved: savedValue };  // Request body with the new 'saved' value

    // Make the PATCH request to the Flask API
    return this.http.patch<any>(url, body);
  }

  changeRating(id: number, rating: number): Observable<any> {
    const url = `${this.apiUrl}/api/item/${id}/rating`;  // Build the API URL with the item ID
    const body = { rating: rating };  // Request body with the new 'saved' value

    // Make the PATCH request to the Flask API
    return this.http.patch<any>(url, body);
  }
}