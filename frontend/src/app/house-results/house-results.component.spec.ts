import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HouseResultsComponent } from './house-results.component';

describe('HouseResultsComponent', () => {
  let component: HouseResultsComponent;
  let fixture: ComponentFixture<HouseResultsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HouseResultsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HouseResultsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
