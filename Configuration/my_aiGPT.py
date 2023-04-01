import os
import shutil

def create_directory_structure(project_name):
    """Create a directory structure for a project based on its key elements and components.

    Args:
        project_name (str): The name of the project.

    Returns:
        None
    """
    # Check if project directory already exists
    if os.path.exists(project_name):
        raise Exception(f"Directory {project_name} already exists. Please choose a different project name.")

    # Create top-level project directory
    try:
        os.mkdir(project_name)
    except OSError as e:
        raise Exception(f"Error creating project directory {project_name}. Error message: {e.strerror}")

    # Create subdirectories for different project components
    subdirectories = [('code', [('python', None), ('javascript', None), ('css', None)]),
                      ('design', [('wireframes', None), ('mockups', None)]),
                      ('data', [('images', None), ('datasets', None)]),
                      ('resources', [('neural_networks', None), ('models', None), ('videos', None)])]

    for subdir, contents in subdirectories:
        try:
            os.mkdir(os.path.join(project_name, subdir))
        except OSError as e:
            raise Exception(f"Error creating directory {subdir} within {project_name}. Error message: {e.strerror}")

        for subsubdir, files in contents:
            try:
                os.mkdir(os.path.join(project_name, subdir, subsubdir))
            except OSError as e:
                raise Exception(f"Error creating directory {subsubdir} within {subdir} of {project_name}. Error message: {e.strerror}")

            if files:
                for file in files:
                    try:
                        open(os.path.join(project_name, subdir, subsubdir, file), "w").close()
                    except OSError as e:
                        raise Exception(f"Error creating file {file} within {subsubdir} of {subdir} in {project_name}. Error message: {e.strerror}")

    # Create subdirectories within code directory
    try:
        os.mkdir(os.path.join(project_name, "code", "python", "ai"))
    except OSError as e:
        raise Exception(f"Error creating directory 'ai' within 'python' of 'code' in {project_name}. Error message: {e.strerror}")

    # Copy a default README file into the project directory
    try:
        default_readme_path = os.path.join(os.getcwd(), "default_readme.txt")
        shutil.copy(default_readme_path, os.path.join(project_name, "README.txt"))
    except Exception as e:
        raise Exception(f"Error copying default README file to {project_name}. Error message: {e}")

    print(f"Directory structure for {project_name} created successfully.")
