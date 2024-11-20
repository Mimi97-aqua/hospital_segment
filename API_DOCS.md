# API Docs

Base URL: `https://hospital-segment.onrender.com`

#### Endpoints

Example request route:
`POST https://hospital-segment.onrender.com/caregiver/create`

**Note:** _The participant here is also referred to as the **patient**._

1. **Create caregiver** _POST_ `caregiver/create/`

![img.png](img.png)

2. **View all caregiver detail:s** _GET_ `caregiver/details`

![img_1.png](img_1.png)

3. **List all participants assigned to a caregiver:** _GET_ `/caregiver/<string:caregiver_id>/participants` 

![img_2.png](img_2.png)

4. **List all prescriptions per participant:** _GET_ `/participant/prescriptions/<string:participant_id>`

**Note:** _action_ is false when a prescription gets created until the administer prescription endpoint is hit.
![img_3.png](img_3.png)

5. **Administer prescription:** _POST_ participant/administer/<string:participant_id>/prescription/<int:prescription_id>

![img_4.png](img_4.png)

6. **List all drugs:** _GET_ `/drugs`

![img_5.png](img_5.png)

7. **List all pharmacies:** _GET_ `/pharmacy`

![img_6.png](img_6.png)

8. **Create participant: ** _POST_ `/participant/create/<string:caregiver_id>`

![img_7.png](img_7.png)

9. **Participant list**: _GET_ `/participant/list`

This lists just the name (first names and last names combined), phone, address, and date of birth of the participant.

![img_8.png](img_8.png)

10. **List all participant details:** _GET_ `/participant/details`

Unlike the precious endpoint, this lists the full participant details

![img_9.png](img_9.png)

11. **Update participant details: ** _PATCH_ `/participant/update/<string:participant_id>`

**Note:** This is a partial update where can only edit their profile photo, legal status and downwards as per the form
in the design. The first 4 fields cannot be edited.

![img_11.png](img_11.png)

![img_12.png](img_12.png)

12. **Delete participant:** _DELETE_ `participant/delete/<string:participant_id>`

![img_folder_for_api_docs/img_13.png](img_folder_for_api_docs/img_13.png)

13. **Create prescription: ** _POST_ `/participant/prescribe`

![img_14.png](img_14.png)

### Test out APIs

To test out the APIs, visit this link to view the [Postman collection.](https://lunar-satellite-35635.postman.co/workspace/My-Workspace~74c77565-9011-4541-82dc-8d69a497f4db/collection/33878300-d1faaabe-c978-4e38-a34e-0956c09b43af?action=share&creator=33878300)
