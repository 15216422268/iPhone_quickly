import Quartz
import AppKit

app_name = 'iPhone镜像'


def get_windows_with_title():
    # 获取所有窗口
    options = Quartz.kCGWindowListOptionOnScreenOnly
    windows = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID)

    for window in windows:
        if window.get('kCGWindowOwnerName', '') == app_name:
            return window.get('kCGWindowBounds')


# 激活窗口
def activate_window():
    """
    激活具有指定标题的窗口
    """
    app = AppKit.NSWorkspace.sharedWorkspace().runningApplications()
    for app_instance in app:
        # 检查窗口标题是否包含目标字符串
        if app_instance.localizedName() == app_name:
            # print(app)
            # 激活窗口
            app_instance.activateWithOptions_(AppKit.NSApplicationActivateIgnoringOtherApps)


def is_iphone():
    active_app = AppKit.NSWorkspace.sharedWorkspace().activeApplication()
    return active_app['NSApplicationName'] == app_name
