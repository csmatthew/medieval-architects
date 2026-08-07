# PROJECT_PLAN.md
<a name="top"></a>

## Table of Contents

- [1. Project Overview](#1-project-overview)
- [2. Goals & Scope](#2-goals--scope)
- [3. Data Model](#3-data-model)
- [4. Site Architecture](#4-site-architecture)
- [5. Template Structure](#5-template-structure)
- [6. Map UX Plan](#6-map-ux-plan)
- [7. Design System](#7-design-system)
- [8. Development Phases](#8-development-phases)
- [9. Milestones](#9-milestones)
- [10. Task Checklist](#10-task-checklist)
- [11. Future Enhancements](#11-future-enhancements)


## 1. Project Overview
A digital prosopography of medieval architects, masons, and builders.  
The project provides structured biographical data, building records, geographic mapping, and scholarly metadata, presented through a clean, archival design inspired by manuscript culture and academic gazetteers.

**Mission:**  
To create a modern, research‑grade digital atlas of medieval architectural makers.

[Back to top](#top)


---

## 2. Goals & Scope

### In scope (Phase 1)
- People list + detail pages  
- Buildings list + detail pages  
- Map (Atlas) with markers and popups  
- Search functionality  
- Basic scholarly styling  
- Basic sources/bibliography  
- Clean template structure  

### Out of scope (future phases)
- Timelines  
- Relationship graphs  
- Manuscript viewer  
- Image galleries  
- API endpoints  
- User accounts  
- Region‑based browsing  
- Advanced filtering  

[Back to top](#top)

---

## 3. Data Model

### Person
- `name`  
- `slug`  
- `roles`  
- `dates_active`  
- `sources`  
- Relationship: Person ↔ Building (via Role)

### Building
- `name`  
- `slug`  
- `county`  
- `location_description`  
- `dates`  
- `sources`  
- Relationship: Building ↔ GeoRef  
- Relationship: Building ↔ Person

### GeoRef
- `latitude`  
- `longitude`  
- `county`  
- `place_name`  
- `precision`  
- Relationship: GeoRef ↔ Building

### Role
- `title` (master mason, architect, overseer)  
- `person`  
- `building`  
- `dates`

### Sources
- `citation`  
- `type` (book, article, manuscript)  
- `link` (optional)

### Notes on uncertain dates
Support formats like:
- `c. 1250`  
- `before 1320`  
- `after 1180`  
- `1250–1270?`

[Back to top](#top)

---

## 4. Site Architecture

### Pages
- Home  
- About  
- People list  
- Person detail  
- Buildings list  
- Building detail  
- Map (Atlas)  
- Search  
- Sources  

### URL structure
```
/people/
/people/<slug>/
/buildings/
/buildings/<slug>/
/map/
/search/
```

### Navigation
- Top navigation bar  
- Breadcrumbs on detail pages  
- Footer with links  

[Back to top](#top)


---

## 5. Template Structure
```
templates/
base.html
layout/
header.html
footer.html
sidebar.html
people/
person_list.html
person_detail.html
buildings/
building_list.html
building_detail.html
mapper/
map.html
```

Principles:
- All main templates live at project level  
- Apps contain logic, not presentation  
- Consistent layout across all pages  
- Reusable components (cards, popups, buttons)

[Back to top](#top)

---

## 6. Map UX Plan

### Map behaviour
- Default view fits to Britain  
- Smooth zoom to building on detail → map transition  
- “Return to Map” button on detail pages  
- Marker clustering for dense regions  
- Sidebar filters (county, type, date)

### Marker styling
- Custom icons inspired by medieval masonry marks  
- Colour palette matches site theme  
- Hover glow + tooltip with building name

### Popup design
- Serif headings  
- Thin ruled divider  
- Building name  
- County  
- Link to detail page  
- Coordinates (optional)

### Tile layer
- Light scholarly theme (recommended)  
- Clean, minimal, archival aesthetic

[Back to top](#top)

---

## 7. Design System

### Colour palette
- Ivory: `#F8F4E8`  
- Ultramarine: `#2F3E9E`  
- Rubrication Red: `#A33F3F`  
- Charcoal: `#2A2A2A`

### Typography
- Headings: EB Garamond or Cormorant  
- Body: Crimson Pro or Alegreya  
- UI fallback: Inter

### Layout
- Two‑column detail pages  
- Metadata sidebar  
- Generous margins  
- Manuscript‑inspired dividers

### Components
- Buttons  
- Cards  
- Map popups  
- Sidebar filters  
- Navigation bar  

[Back to top](#top)

---

## 8. Development Phases

### Phase 1 — Foundation
- Models  
- Admin setup  
- Basic views  
- Basic templates  
- Basic map rendering

### Phase 2 — Styling
- Base layout  
- Typography  
- Colour palette  
- Component library  
- Map popup styling

### Phase 3 — Features
- Search  
- Filters  
- Map → detail → map flow  
- Sources integration

### Phase 4 — Polish
- Accessibility  
- Performance  
- Mobile layout  
- SEO  
- Error pages

### Phase 5 — Content
- Import data  
- Clean data  
- Add sources  
- Add metadata

[Back to top](#top)

---

## 9. Milestones

- Milestone 1: Foundation  
- Milestone 2: Styling  
- Milestone 3: Map  
- Milestone 4: Features  
- Milestone 5: Content  

[Back to top](#top)

---

## 10. Task Checklist

### Models
- [ ] Person model  
- [ ] Building model  
- [ ] GeoRef model  
- [ ] Role model  
- [ ] Sources model  

### Templates
- [ ] base.html  
- [ ] person_list.html  
- [ ] person_detail.html  
- [ ] building_list.html  
- [ ] building_detail.html  
- [ ] map.html  

### Map
- [ ] Marker icons  
- [ ] Popups  
- [ ] Clustering  
- [ ] Return‑to‑map flow  
- [ ] Sidebar filters  

### Styling
- [ ] Colour palette  
- [ ] Typography  
- [ ] Layout grid  
- [ ] Component library  

### Features
- [ ] Search  
- [ ] Filters  
- [ ] Sources section  

### Polish
- [ ] Mobile layout  
- [ ] Accessibility  
- [ ] SEO  

[Back to top](#top)

---

## 11. Future Enhancements
- Timeline visualisation  
- Relationship graph (architect ↔ building ↔ patron)  
- Manuscript viewer  
- Region‑based browsing  
- API endpoints  
- Image galleries  
- Advanced search  
- Patron records  
- 3D reconstructions (Blender + WebGL)


[Back to top](#top)

