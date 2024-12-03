import { Component, OnInit } from '@angular/core';
import { SearchService } from '../services/search.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  standalone: true,
  imports: [CommonModule],
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

    var logsContainer = document.getElementById("logs");
    console.log(logsContainer)
    logsContainer!.innerHTML = "Starting search...\n";
    this.logs.push("Starting search...\n");
    try {
      const response = await fetch('http://localhost:5000/search');
      if (!response.body) {
        logsContainer!.innerHTML += "Streaming not supported.\n";
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
          logsContainer!.innerHTML += chunk;
          this.logs.push(chunk);
          logsContainer!.scrollTop = logsContainer!.scrollHeight; // Auto-scroll to the latest log
        }
      }

      logsContainer!.innerHTML += "\nSearch completed.\n";
    } catch (error) {
      logsContainer!.innerHTML += `\nError: ${error}\n`;

    }
  }
}