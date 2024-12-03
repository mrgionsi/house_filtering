import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'numberFormat',
  standalone: true, // Mark the pipe as standalone
})
export class NumberFormatPipe implements PipeTransform {
  transform(value: number, currencySymbol: string = '€'): string {
    if (value.toLocaleString().toLocaleLowerCase() == "prezzo su richiesta")
      return "Prezzo su richiesta"
    if (value == null || isNaN(value)) {
      return ''; // Return empty string for invalid values
    }

    // Convert the number to a string with European formatting
    const formattedNumber = value
      .toString()
      .replace(/\B(?=(\d{3})+(?!\d))/g, '.'); // Add dots as thousand separators

    return `${currencySymbol} ${formattedNumber}`;
  }
}
