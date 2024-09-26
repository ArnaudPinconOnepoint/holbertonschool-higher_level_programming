#!/usr/bin/python3
"""
0-hbtn_status

This script fetches the status of a website
using urllib with a User-Agent header.
"""

if __name__ == "__main__":
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    headers2 = {"User-Agent": "Mozilla/5.0 (Linux x86_64)", "Cookie": "introjs-dontShowAgain=true; timezone=10; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik16QTNNVEU9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--a4e332e7a660b1de6e9e9f787d5261d4f6168f2c; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1qazEiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--cbb9fb9823fc13cb7c544a7ee1db56b8b315e066; cf_clearance=d86L2dMjda6nCdkMUMG4YttzaBc9huHL_dHNI.KteOY-1727324389-1.2.1.1-SXH.fWjG6aSI_NzOSNiSULz.xRpS0WjvuA45ouAua93.GIXBefn34ASn809ihI2n6HMfyj8sEO6OAYkSzGxVJvkXo0lEEOl2X8QA3rHtaSqUjGgrUcvJOs4nGpn3GJkYZ932YQ0alpqWtUw.7VdIWSzO4Rtfjm8My05Le4QfIkyy21xGhKYy0Mpf8NoKGCIgPNNDCUn47h8qQkPwZjQiwJ563OiasUE6UnJ_SJJdwtLySoocTssWi7DHuTtSta8_jJU83etzK5BsXP6bFwaQYrjsofbzIi.75uvRWqsFa5ALJh.5K3RW21PkfyLEnqUWMT.89IEGypxSZ5wSIRJjSHgwCpLu2f_Nok5f_Aq5pMcW0x8Dl2HXvcdvddeFJGFRw_haZJQo1l0upRjUqlkuy0UQ4cXh_IAq1UenCpbmXNKVUjLg4GyfDHFPT3gV8Y6Z; _holberton_intranet_session=r%2FaDL1vL0%2FPU2wo0MN05dkRTyvxtb0EZqfqedXIr8%2BSTJv5PHPPX%2FViwuPqiuUrS2b9L58CYSIB5CpnNCG9bZ7BgqBRoNQN4DA7waMfRQJ%2BMlvmE1kP9%2BgDBAeJdAfeEmo8YLRupVHvJO9JWif5y9Z%2FnctSREGDL6y6G%2F7eubk1zgq1ZdfCiMMa0zTZnMg89%2FeQkL1gztn0lELY4nIvbJZkfIwS0OOgU0uYFXKIshHX2F%2FDMbWcSXyXTYk3bZtiiXFOQoZ1KNCPP1AHwnVXCQAgcZx%2Bfy6ywW4e%2F2EGE5iICgjpD0p1XLQtyjyffoJ0gxLvfs%2B5%2Fo2K77eW%2BT8EWiDeSz2CMHs0rMsXkUG5b06dS43aqDhViBdzipr3TsazPLVmM0%2F77ySDGQr2AQzxPNxmuw7kzWEKEOKqp49S87bO1zwqCVSIu5TDzqGMyaD88hJX6y1Evl8jyU4OkHer82gHpJnlUaEs%3D--8fMBVC6Qz2ayfxvv--iMAhof%2BUjzerOfDNP4lkNA%3D%3D"}
    request = urllib.request.Request(url, data=None, headers=headers2)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
