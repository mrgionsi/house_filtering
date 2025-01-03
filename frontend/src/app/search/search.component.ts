import { Component, OnInit } from '@angular/core';
import { SearchService } from '../services/search.service';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  standalone: true,
  imports: [CommonModule, ButtonModule],
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  logs: string[] = [];   // Store received logs
  isLoading: boolean = false;

  constructor(private searchService: SearchService) { }

  ngOnInit(): void { }

  async startSearch(): Promise<void> {
    this.isLoading = true;
    this.logs = [];  // Reset logs on each new search

    this.logs.push("Starting search...\n");
    try {
      const response = await fetch(environment.backend_url + '/search');
      if (!response.body) {
        this.logs.push("Streaming not supported.\n");
        return;
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      let done = false;

      while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;
        if (value) {
          const chunk = decoder.decode(value, { stream: true });
          this.logs.push(chunk);
        }
      }

      this.logs.push("\nSearch completed.\n");
      this.isLoading = false;
    } catch (error) {
      this.logs.push(`\nError: ${error}\n`)
      this.isLoading = false;


    }
  }
}