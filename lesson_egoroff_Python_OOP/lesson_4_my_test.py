HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    EP_upload_image_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}/uploadImage"
    EP_add_pet = f"{HOST}/pet"
    EP_update_full_pet = f"{HOST}/pet"
    EP_find_by_status_pet = f"{HOST}/pet/findByStatus"
    EP_find_by_ID_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}"
    EP_update_name_and_status_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}"
    EP_delete_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}"


print(Endpoints.EP_find_by_ID_pet(1,2))
