import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class SettingsService {

  private apiUrl = environment.backend_url + '/api/schedule-task';  // Replace with your Flask API URL

  constructor(private http: HttpClient) { }

  scheduleTask(data: { time: string }): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
