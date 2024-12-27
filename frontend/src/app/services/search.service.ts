import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.development';

@Injectable({
  providedIn: 'root',
})
export class SearchService {
  private apiUrl = environment.backend_url; // Replace with your API URL

  constructor(private http: HttpClient) { }

  // Fetch the streaming response from the API
  getSearchStream(): Observable<string> {
    return this.http.get(this.apiUrl, {
      responseType: 'text', // Expect a text stream
      reportProgress: true,
      observe: 'body',
    });
  }
  setSaved(save: boolean, id: number): Observable<string> {
    return this.http.get(this.apiUrl, {
      responseType: 'text', // Expect a text stream
      reportProgress: true,
      observe: 'body',
    });
  }

}
