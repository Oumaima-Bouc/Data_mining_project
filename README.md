
# Flights Data Documentation

## Overview
This repository contains data related to flights from around 2021. The data is stored in JSON file, with each entry providing detailed information about a specific flight, including operational time, airline, flight number, airports, and terminal details. A `CodeContext` field offers additional metadata to interpret specific attributes. Additional descriptive files in `xml` format offer complete details for specific flights on a given day (we actually have only those of day-2).


## Data Structure
Each flight entry in the JSON file follows this structure:

```json
{
  "operationtime": "2021-12-29 16:49:00",
  "airline": "AH",
  "flightnumber": "1011",
  "departureairport": "ORY",
  "arrivalairport": "ALG",
  "aircraftterminal": "4",
  "departureorarrival": "Arrival",
  "origindate": "2021-12-29",
  "CodeContext": "ONB"
}
```

### Field Descriptions
- **operationtime**: The exact time of the flight operation (departure or arrival) in `YYYY-MM-DD HH:MM:SS` format.
- **airline**: The airline operating the flight, represented by a two-letter code (e.g., `AH` for Air Algérie).
- **flightnumber**: The number assigned to the flight by the airline.
- **departureairport**: The code for the departure airport (e.g., `ORY` for Orly, Paris).
- **arrivalairport**: The code for the arrival airport (e.g., `ALG` for Algiers, Houari Boumediene Airport).
- **aircraftterminal**: The terminal number at the departure or arrival airport.
- **departureorarrival**: Specifies whether the record is for a departure or arrival flight.
- **origindate**: The date the flight originates in `YYYY-MM-DD` format.
- **CodeContext**: A code providing additional context or metadata for interpreting the record (e.g., `ONB`).

## Data Updates
- The dataset can be updated daily with a new `xml` file containing the complete description of flights for "day-2."


## Usage
1. **Understanding the Codes**: Use the `CodeContext` field to interpret additional metadata. A separate file describe the meaning of each `CodeContext` value (e.g., `ONB`).

## Example Entry
A flight arriving in Algiers (ALG) from Orly (ORY), operated by Air Algérie (AH) on December 29, 2021, would appear as:

```json
{
  "operationtime": "2021-12-29 16:49:00",
  "airline": "AH",
  "flightnumber": "1011",
  "departureairport": "ORY",
  "arrivalairport": "ALG",
  "aircraftterminal": "4",
  "departureorarrival": "Arrival",
  "origindate": "2021-12-29",
  "CodeContext": "ONB"
}
```

## Contributions
If you have questions, clarifications, or additions to the dataset, please don't hesitate to contact me .
