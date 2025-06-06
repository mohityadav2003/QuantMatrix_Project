﻿# EDA Dashboard

## Project Overview
This project is an interactive EDA (Exploratory Data Analysis) Dashboard built with React and Material-UI for the frontend, and a backend API that serves data for various business metrics. The dashboard allows users to filter and visualize sales, volume, trends, and market share data using modern, responsive charts and UI components.

## Tech Stack Used
- **Frontend:** React, Material-UI (MUI), Recharts, Axios
- **Backend:** (Assumed) Python/Django or Node.js/Express (API endpoints)
- **Other:** JavaScript (ES6+), HTML5, CSS3

## Approach Used
- **Component-Based UI:** The dashboard is built using React functional components, leveraging hooks for state and lifecycle management.
- **Data Fetching:** Axios is used to fetch filter options and dashboard data from RESTful API endpoints. Filters are dynamically populated based on backend data.
- **Responsive Design:** Material-UI's Grid system and Card components are used for a clean, responsive layout. Recharts provides interactive, responsive charts.
- **Separation of Concerns:** UI logic, data fetching, and rendering are kept modular and maintainable.

## Key Decisions Taken
- **Dynamic Filters:** Filters are populated from the backend, ensuring scalability as new brands, years, or categories are added.
- **RESTful API Integration:** All data is fetched via API endpoints, making the dashboard backend-agnostic and easy to extend.
- **Modern UI/UX:** Material-UI and custom styling are used for a modern, user-friendly interface. Cards, spacing, and color choices are made for clarity and visual appeal.
- **Charting Library:** Recharts was chosen for its ease of use, responsiveness, and integration with React.

## Thought Process
- **User Experience:** The dashboard is designed to be intuitive, with filters at the top and key metrics visualized in a grid below. The layout is responsive for different screen sizes.
- **Maintainability:** Code is organized for easy updates, with clear separation between data fetching, state management, and rendering.
- **Scalability:** The approach allows for easy addition of new filters, charts, or data sources.
- **Performance:** Only relevant data is fetched based on active filters, reducing unnecessary network requests and improving performance.

## Folder Structure
```
EDA-main/
├── client/
│   ├── src/
│   │   └── App.js         # Main dashboard component
│   └── ...                # Other React files and configs
├── server/                # (Optional) Backend API code
└── README.md
```
