import pkg_resources

package_name = 'tensorflow'
installed_packages = {pkg.key for pkg in pkg_resources.working_set}
if package_name in installed_packages:
    print(f"{package_name} is installed.")
else:
    print(f"{package_name} is not installed.")