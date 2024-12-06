import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { SettingsService } from '../services/settings.service';
import { CalendarModule } from 'primeng/calendar';
import { ButtonModule } from 'primeng/button';
import { firstValueFrom } from 'rxjs';
import { DropdownModule } from 'primeng/dropdown';
import { DateTime } from 'luxon';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [ButtonModule, CalendarModule, DropdownModule, FormsModule],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.scss'
})
export class SettingsComponent {
  selectedTime: Date = new Date();  // Default to current time
  selectedFrequency: string = 'daily';  // Default frequency
  frequencyOptions = [
    { label: 'Every day', value: 'daily' },
    { label: 'Once per week', value: 'weekly' },
    { label: 'Twice per week', value: 'twice-weekly' },
    { label: 'Once per month', value: 'monthly' },
    { label: 'Custom cron expression', value: 'custom' }
  ];

  constructor(private settingsService: SettingsService) { }

  // Method to call the service and schedule the job
  async scheduleJob() {
    if (this.selectedTime) {
      console.log(this.selectedTime)
      // Get the date in Italy's time zone
      const italianTime = DateTime.fromJSDate(this.selectedTime).setZone('Europe/Rome');

      // Format the time in ISO 8601 format (with Z at the end for UTC)
      const scheduledTime = italianTime.toISO() || ""; // This will give the ISO string with time zone
      const requestBody = { time: scheduledTime };
      console.log(requestBody)

      try {
        const response = await firstValueFrom(this.settingsService.scheduleTask(requestBody));
        console.log('Task scheduled successfully:', response);
      } catch (error) {
        console.error('Error scheduling task:', error);
      }
    } else {
      console.error('No time selected!');
    }
  }
}