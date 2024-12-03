import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { Item } from '../models/item.model'; // Adjust the path as necessary

@Injectable({
  providedIn: 'root'
})
export class ItemDataService {
  private apiUrl = 'http://127.0.0.1:5000'; // Correctly formatted URL

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
}