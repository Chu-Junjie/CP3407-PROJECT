# CP3407---Smart Digital Product Recommendation Platform

Welcome to the Smart Digital Product Recommendation Platform repository. This project aims to help users find the most suitable digital products (e.g., laptops, smartphones, peripherals) that fit their budget and needs through intelligent and personalized assessment algorithms, simplifying the decision-making process in a tech market filled with overwhelming information.

🌟 **Live Demo:** [Click here to experience our Iteration 1 Platform](https://chu-junjie.github.io/CP3407-PROJECT/)

---

## 1. Project Overview
In today's tech market, digital products iterate rapidly with complex specifications. Average consumers often face "choice paralysis" and information overload. This project will develop a web-based smart digital product recommendation platform. Users only need to complete a short interactive questionnaire. The platform will then filter and match products from the database using a core recommendation algorithm, providing users with intuitive quantitative recommendation scores and comprehensive spec comparisons to simplify their decision-making process.

---

## 2. Objectives
* **Accurate Matching:** Build a recommendation algorithm engine capable of efficient matching based on user inputs (e.g., primary use case, budget, brand preference, hardware requirements).
* **User-Friendly Interface:** Create a highly available, responsive web frontend providing intuitive product discovery, comparison, and visual charts.
* **Stable Infrastructure:** Establish secure and scalable backend and database services to support the storage of hardware specs, efficient queries, and the security of user data.

---

## 3. Features
* **Smart Assessment:** Provide a quick, intuitive, personalized questionnaire (e.g., budget range, primary scenarios like 3D modeling/gaming/office work, portability or battery life preferences).
* **Personalized Recommendations:** Display the top 3 recommended digital products based on matching scores, along with reasons for the recommendation.
* **Product Comparison:** Allow users to compare multiple recommended products side-by-side, clearly displaying core specs like CPU, GPU, RAM, and price in a table format.
---

## 4. Technology Stack
* **Frontend:** to be confirmed
* **Backend:** Python 
* **Database:** to be confirmed
* **Design/UI:** Figma (for rapid prototyping and testing based on Lean UX principles)
* **IDE & Tools:** Git/GitHub, PyCharm
---

## 5. Team Members & Roles
This project is collaboratively developed by a team of 4 members. The specific roles and responsibilities are as follows:

| Name | Project Role | Key Responsibilities |
| :--- | :--- | :--- |
| **Junjie Chu** | Project Manager | Overall project schedule management, task allocation, agile iteration advancement, and writing Practical reports. |
| **Guanyu Lu** | UI/UX Designer & Frontend Developer | UI/UX interaction design (Figma prototypes), frontend page development, and component interaction implementation. |
| **Zaikun Zheng**| Backend & Algorithm Engineer | Backend API development, core recommendation algorithm, and matching logic design/implementation. |
| **Yuyang Zhou** | Database Administrator | Digital product dataset cleaning, database schema design, AWS/local database deployment, and performance tuning. |

---

## 6. Milestone 1 & Iteration Planning

To effectively manage our development cycle and deliver a high-quality product, we have structured Milestone 1 into three distinct iterations based on user story priorities and effort estimations. 

### 🌟 Iteration 1: MVP Core Pipeline (Total Effort: 36 Days)
* **Goal:** Successfully run the core data flow: "Database Setup -> Natural Language Input Processing -> Recommendation Leaderboard Display".
* **Current Focus:** Week 3 Practical Target.

| ID | Title | User Story | Priority | Effort (Days) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US-01** | Natural Language Needs Description | **As a** consumer with limited hardware knowledge, **I want to** describe my usage habits in everyday natural language (e.g., "a durable phone with a big screen for my mom"), **so that** the system can understand my real needs without requiring me to research technical specs. | 10 | 12 | 🟢 Done |
| **US-02** | Database Setup & Import | **As a** system administrator, **I want to** import a digital product dataset (e.g., CSV format) into the database, **so that** the platform has enough underlying data to support queries and recommendations. | 10 | 10 | 🟢 Done |
| **US-03** | Customized Leaderboard | **As a** buyer looking for a new device, **I want to** see a Top 5 recommended leaderboard immediately after entering my needs, clearly displaying the matching percentage, **so that** I can intuitively compare and make a quick purchasing decision. | 10 | 14 | 🟢 Done |

### ⏱️ Actual Velocity Calculation for Iteration 1
Velocity is a measure of how much work our team successfully completed in this iteration. We only count the estimates of *100% completed* user stories.

* US-01 Estimate: 12 Days (Completed)
* US-02 Estimate: 10 Days (Completed)
* US-03 Estimate: 14 Days (Completed)

**Actual Velocity = 12 + 10 + 14 = 36 Days**

**Conclusion:** Our team's actual velocity for Iteration 1 exactly matches our initial planned capacity (36 Days). This proves that our task breakdowns and estimations were highly accurate, giving us a reliable baseline (Velocity = 36/20*4=0.45) for planning Iteration 2!

### 📉 Burn Down Graph
Below is the Burn Down Graph for tracking the remaining effort during Iteration 1. The total estimated effort starts at 11 days and is planned to burn down linearly to 0 by Day 10.

```mermaid
xychart-beta
    title "Iteration 1 Burn Down Graph"
    x-axis "Days Left" [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
    y-axis "Work Left (Days)" 0 --> 40
    line "Ideal Trend" [36, 32.4, 28.8, 25.2, 21.6, 18.0, 14.4, 10.8, 7.2, 3.6, 0]
    bar "Actual Remaining" [36, 36, 36, 26, 26, 26, 14, 14, 14, 14, 0]
```
### Document: Completed vs. Unfinished User Stories (Iteration 1 Review)
At the end of Iteration 1, we conducted a Sprint Review to evaluate our deliverables against our initial commitments.

**✅ Completed User Stories (Total: 36 Days)**
* **US-01 (12 Days):** MVP Frontend UI for natural language input is fully functional.
* **US-02 (10 Days):** Database setup and initial digital product dataset imported successfully.
* **US-03 (14 Days):** Frontend leaderboard dynamically renders top recommendations based on mock integrated data.

**❌ Unfinished User Stories (Total: 0 Days)**
* *None.* All planned tasks for Iteration 1 were 100% successfully executed and merged into the main branch. No technical debt or unfinished stories need to be carried over to Iteration 2.
---

### 🔍 Iteration 2: Decision Support & Feature Filtering (Total Effort: 36 Days)
* **Goal:** Enhance recommendation transparency and implement advanced preference filtering.

| ID | Title | User Story | Priority | Effort (Days) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US-04** | Personalized Explanation | **As a** skeptical user, **I want to** read a one-sentence, easy-to-understand explanation below each recommended product, **so that** I understand exactly why it was matched to me and can trust the recommendation. | 20 | 13 | 🟢 Done |
| **US-05** | Product Spec Comparison | **As a** consumer, **I want to** select multiple products and view their hardware specs side-by-side in a table format, **so that** I can intuitively see the differences in components like RAM and processors. | 20 | 10 | 🟢 Done|
| **US-06** | Exclude Unwanted Features | **As a** user with strict personal preferences, **I want to** list features I absolutely cannot accept (e.g., "no curved screens"), **so that** the system automatically filters out products with these dealbreakers. | 30 | 13 | 🟢 Done |

### ⏱️ Actual Velocity Calculation for Iteration 2
At the end of Iteration 2, our team successfully completed all planned tasks focusing on decision support and filtering. 

* **US-04 Estimate:** 13 Days (Completed)
* **US-05 Estimate:** 10 Days (Completed)
* **US-06 Estimate:** 13 Days (Completed)

**Actual Velocity = 13 + 10 + 13 = 36 Ideal Days**

**Reflection:** Our actual velocity (36 Days) perfectly matches our projected capacity. This indicates our team's estimation accuracy and focus factor (36/(20*4)=0.45) have stabilized. We will use this exact velocity of **36 Days** as the rigid baseline to plan our final sprint (Iteration 3).

### 📉 Iteration 2 Burn Down Graph
Below is the Burn Down Graph for Iteration 2. The effort started at 36 days and successfully burned down to 0, demonstrating a healthy Agile cadence where tasks were sequentially moved to 'Done'.

```mermaid
xychart-beta
    title "Iteration 2 End-of-Sprint Burn Down"
    x-axis "Days Left" [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
    y-axis "Work Left (Days)" 0 --> 40
    line "Ideal Trend" [36, 32.4, 28.8, 25.2, 21.6, 18.0, 14.4, 10.8, 7.2, 3.6, 0]
    bar "Actual Remaining" [36, 36, 36, 23, 23, 23, 13, 13, 13, 13, 0]
```
---

### 🚀 Iteration 3: Conversion, Feedback & Sharing (Total Effort: 36 Days)
* **Goal:** Implement external e-commerce redirection, social sharing, and user feedback loops for continuous algorithm improvement.
 
Based on our Iteration 2 Actual Velocity of 36 Days, we have updated the backlog for Iteration 3 to exactly match this capacity.

| ID | Title | User Story | Priority | Effort (Days) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US-07** | Direct Purchase Links | **As an** eager buyer, **I want to** click on a recommended product to be redirected to official e-commerce stores, **so that** I can make a purchase directly without manually searching for it elsewhere. | 40 | 7 | 🟡 In-Progress |
| **US-08** | Feedback Mechanism | **As an** engaged user, **I want to** click a "thumbs up" or "thumbs down" button at the bottom of the leaderboard, **so that** I can provide feedback to the developers to improve future algorithm accuracy. | 40 | 7 | 🟡 In-Progress |
| **US-09** | Budget Alternatives | **As a** budget-conscious consumer, **I want to** see a cheaper "budget alternative" for top-tier expensive recommendations, **so that** I can save money without sacrificing core experiences. | 50 | 12 | 🟡 In-Progress |
| **US-10** | Share Leaderboard | **As a** user helping family or friends choose a device, **I want to** generate a shareable link of the customized leaderboard, **so that** I can easily send the tailored recommendation results for them to view on their own devices. | 50 | 10 | 🟡 In-Progress |

**Total Iteration 3 Effort Estimate = 7 + 7 + 12 + 10 = 36 Days** *(Perfectly aligned with team velocity!)*

---

## 7. System Architecture & Modeling

To ensure a robust and scalable platform, we have utilized UML modeling to represent the core domain logic and the runtime interactions between our frontend UI, backend engine, and database.

### 🧩 Class Diagram
The static structure below illustrates the main entities of our recommendation platform and their relationships:
```mermaid
classDiagram
    class UserPreference {
        +String rawTextIntent
        +double budgetLimit
        +List~String~ excludedFeatures
        +extractKeywords()
    }

    class Product {
        +String productID
        +String name
        +String specs
        +double price
        +String category
        +getDetails()
    }

    class RecommendationEngine {
        +calculateMatchScore(UserPreference, Product) double
        +sortAndFilter(List~Product~) List~Product~
    }

    class DatabaseManager {
        +connectToDB()
        +fetchProductsByCategory(String) List~Product~
    }

    class FrontendController {
        +captureUserInput()
        +renderLeaderboard(List~Product~)
    }

    FrontendController --> UserPreference : creates
    FrontendController --> RecommendationEngine : requests match
    RecommendationEngine --> DatabaseManager : fetches
    DatabaseManager --> Product : returns
    RecommendationEngine --> Product : evaluates
```
### 🔎 Design Principles Check (SRP & DRY)
During the end of Iteration 1, we reviewed our Class Diagram against the core principles from Chapter 5:

**1. Single Responsibility Principle (SRP):**
*Our classes satisfy SRP because each class has only one reason to change:*
* `DatabaseManager`: Only handles database connection and raw data fetching. It does not care about how products are matched or displayed.
* `RecommendationEngine`: Only handles the mathematical matching logic (calculating scores).
* `FrontendController`: Strictly focuses on capturing user input and rendering the UI. It delegates all heavy lifting to the Engine.

**2. Don't Repeat Yourself (DRY):**
*We applied the DRY principle in our frontend code:*
* Instead of writing duplicate HTML code for each of the Top 5 products, we created a single reusable JavaScript function `renderLeaderboard(data)`. It iterates through the array and dynamically generates the UI components, ensuring that if we want to change the card style in the future, we only need to update the code in one place.

### 🔄 Sequence Diagram
The dynamic behavior below maps out the execution flow of US-01 to US-03, showing how natural language input gets processed into a Top 5 leaderboard:

```mermaid
sequenceDiagram
    actor User
    participant UI as Frontend (Guanyu)
    participant Engine as RecEngine (Zaikun)
    participant DB as Database (Yuyang)

    User->>UI: Types "I need a gaming laptop under $1500"
    User->>UI: Clicks "Find My Device"
    activate UI
    UI->>UI: Display Loading Spinner
    UI->>Engine: POST /api/recommend (userIntent)
    activate Engine
    Engine->>DB: Query Laptops <= $1500
    activate DB
    DB-->>Engine: Return Raw Laptop List
    deactivate DB
    Engine->>Engine: Calculate Match % for each
    Engine->>Engine: Sort Top 5
    Engine-->>UI: Return JSON (Top 5 Products)
    deactivate Engine
    UI->>UI: Hide Loading Spinner
    UI->>UI: Render Leaderboard HTML
    UI-->>User: Display Top 5 Recommendations
    deactivate UI
```
---
## 8. Data and Privacy
* The digital product specifications (e.g., price, processor, GPU, RAM) used by this platform are sourced from public channels or open-source datasets.
* The platform strictly adheres to privacy protection principles. All preference data inputted by users in the questionnaire is only used for real-time calculation of the current recommendation and will never be disclosed to any third party without permission.

## 9. Testing Strategy & Test-Driven Development (TDD)

### 🧪 Testing Plan (Based on TDD Principles)
In Iteration 2, we adopted **Test-Driven Development (TDD)** as our primary engineering practice. Before implementing new features, we write automated tests to define the desired behavior. Our testing strategy includes:
1. **Unit Testing:** We test individual Python functions (e.g., `parse_budget_from_text`) in isolation to ensure logic algorithms are mathematically and logically correct.
2. **Integration Testing:** We test the Flask API endpoints combined with the SQLite database to ensure the system correctly fetches, filters, and returns JSON payloads.
3. **Acceptance Testing:** We map our tests directly to the Acceptance Criteria of our User Stories to guarantee business value delivery.

### 📋 Test Cases (15 Cases across 5 User Stories)
Below are 15 carefully designed test cases covering both completed (US-01, 02, 03) and upcoming (US-04, 06) user stories, following the exact standard from the textbook.

| User Story | Test Case ID | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| **US-01: NLP Input** | TC-01.1 | Input contains explicit budget ("under $1000") | System successfully extracts `1000` as the budget limit. |
| | TC-01.2 | Input contains NO budget ("I want a gaming laptop") | System assigns the default max budget ($5000). |
| | TC-01.3 | Input contains non-standard symbols ("below 1,500 bucks") | System correctly parses `1500` despite natural language noise. |
| **US-02: DB Setup** | TC-02.1 | Initialize empty database on startup | System automatically reads CSV and creates the SQLite table. |
| | TC-02.2 | Check `/api/health` endpoint | Returns HTTP 200 with the exact row count of the database. |
| | TC-02.3 | Prevent duplicate imports | Running setup twice does not duplicate records in the database. |
| **US-03: Leaderboard**| TC-03.1 | Request recommendations | API returns exactly 5 (or fewer) product items in a JSON array. |
| | TC-03.2 | Verify sorting order | The returned JSON array is strictly sorted by `match_score` descending. |
| | TC-03.3 | Verify budget constraint | All 5 returned products have a price lower than or equal to the user's budget. |
| **US-04: Explanation**| TC-04.1 | Verify reason payload | The JSON response object contains a `reason` string field. |
| | TC-04.2 | Specific feature match | If user asks for "gaming", the reason string contains the keyword "Gaming". |
| | TC-04.3 | Generic fallback explanation | If no specific feature matches, reason defaults to "general product match". |
| **US-06: Exclusions** | TC-06.1 | Parse negative keywords ("no Apple") | System identifies "Apple" as an excluded brand/feature. |
| | TC-06.2 | Verify exclusion filtering | The returned JSON array contains exactly ZERO products from the excluded brand. |
| | TC-06.3 | Case-insensitive exclusion | "apple" and "APPLE" both successfully trigger the exclusion logic. |
