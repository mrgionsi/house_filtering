import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SettingsService {

  private apiUrl = 'http://127.0.0.1:5000/api/schedule-task';  // Replace with your Flask API URL

  constructor(private http: HttpClient) { }

  scheduleTask(data: { time: string }): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
