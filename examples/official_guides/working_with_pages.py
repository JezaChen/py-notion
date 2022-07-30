""" Interactive API sample code for interacting with pages """

from examples.official_guides.common_prelude import get_client_and_base_page_id
from examples.official_guides.data import PageExampleData
from examples.utils import colored_print, PrintStyle, generate_step_printer, press_enter_to_continue

print_step = generate_step_printer()

client, base_page_id = get_client_and_base_page_id()

##############################################
# Create a page as a child of the page given #
##############################################

print_step("Create a page as a child of the page given")

page_create_body_data = PageExampleData.CREATE_EXAMPLE.copy()
page_create_body_data["parent"]["page_id"] = base_page_id  # Fill the page_id of the parent

page_create_rsp = client.pages.create(page_create_body_data)
print(f"--- Page Create Result ---\n"
      f"{page_create_rsp}\n"
      f"--- Page Create Result ---")

page_id: str = page_create_rsp["id"]

colored_print(f"The newly added page can be viewed as https://www.notion.so/{page_id.replace('-', '')}")

press_enter_to_continue()
###################
# Update the page #
###################

print_step("Update the title of this page")
page_update_rsp = client.pages.update(page_id,
                                      PageExampleData.UPDATE_EXAMPLE)

print(f"--- Page Update Result ---\n"
      f"{page_update_rsp}\n"
      f"--- Page Update Result ---")

colored_print(f"The title of this page is changed to "
              f"`{PageExampleData.UPDATE_EXAMPLE['properties']['title']}` successfully. "
              f"You can now view the intuitive result by clicking on the following links: "
              f"https://www.notion.so/{page_id.replace('-', '')}",
              color=PrintStyle.GREEN)

press_enter_to_continue()
###################
# Delete the page #
###################

print_step("Delete this page")
page_delete_rsp = client.blocks.delete(page_id)

print(f"--- Page Update Result ---\n"
      f"{page_delete_rsp}\n"
      f"--- Page Update Result ---")

colored_print(f"The example page is deleted successfully. "
              f"You can now view the intuitive result by backing to your test page: "
              f"https://www.notion.so/{base_page_id}",
              color=PrintStyle.GREEN)
