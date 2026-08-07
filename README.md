# Medieval Architects Atlas
<a name="top"></a>




A digital prosopography and geographic atlas of medieval architects, masons, and builders.  
This project combines structured biographical data, building records, and geospatial mapping to create a modern, research‑grade resource inspired by manuscript culture and academic gazetteers.

## Table of Contents

- [Project Purpose](#project-purpose)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Map Overview](#map-overview)
- [Data Model Summary](#data-model-summary)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)



[Back to top](#top)

---

## Project Purpose

The Medieval Architects Atlas aims to:

- Document medieval architectural makers (architects, masons, overseers)
- Catalogue buildings associated with them
- Provide geographic visualisation through an interactive map
- Present scholarly metadata in a clean, archival design
- Support future research, teaching, and digital humanities work

[Back to top](#top)

---

## Features

### Core (Phase 1)
- People list + detail pages  
- Buildings list + detail pages  
- Interactive map (Atlas)  
- Marker clustering + popups  
- Search functionality  
- Clean template structure  
- Basic scholarly styling  

### Planned (Future Phases)
- Timelines  
- Relationship graphs  
- Manuscript viewer  
- Region‑based browsing  
- API endpoints  
- Image galleries  

[Back to top](#top)

---

## Tech Stack

- **Python / Django** — backend framework  
- **Leaflet.js** — interactive mapping  
- **PostgreSQL** (recommended) — spatially friendly database  
- **HTML / CSS / JS** — templating and UI  
- **GitHub Projects** — Kanban workflow  
- **GitHub Issues** — task tracking  

[Back to top](#top)

---

## Project Structure

```
project/
core/
buildings/
people/
mapper/
templates/
base.html
layout/
people/
buildings/
mapper/
static/
PROJECT_PLAN.md
README.md
```
[Back to top](#top)

---

## Map Overview

The Atlas uses Leaflet.js to display:

- Building markers  
- Custom medieval‑inspired icons  
- Popups with building metadata  
- Smooth transitions between map → detail → map  
- Sidebar filters (planned)  

[Back to top](#top)

---

## Data Model Summary

### Person
Architect, mason, or master of works.

### Building
Structure associated with one or more people.

### GeoRef
Geographic coordinates + location metadata.

### Role
Defines the relationship between a person and a building.

### Sources
Bibliographic references.

Full details are in `PROJECT_PLAN.md`.

[Back to top](#top)

---

## Getting Started

### 1. Clone the repository
```
git clone <repo-url>
cd medieval-architects
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run migrations
```
python manage.py migrate
```
### 4. Start the development server
```
python manage.py runserver
```
[Back to top](#top)

---

## Development Workflow

This project uses:

- **GitHub Projects** for Kanban  
- **GitHub Issues** for tasks  
- **Milestones** for phases  
- **Feature branches** for development  

See `PROJECT_PLAN.md` for full planning documentation.

[Back to top](#top)

---

## Contributing

Contributions are welcome.  
Please:

1. Open an Issue  
2. Create a feature branch  
3. Submit a Pull Request  
4. Link your PR to the relevant Issue or Milestone  

[Back to top](#top)

---

## License

This project is released under the MIT License.  
See `LICENSE` for details.

[Back to top](#top)

---

## Acknowledgements

Inspired by medieval architectural history, digital humanities practice, and the tradition of scholarly prosopography.

[Back to top](#top)
