import sys
import torch


def check_environment():
    print("✅ Python 解释器路径：", sys.executable)
    print("✅ Python 版本：", sys.version)

    try:
        print("✅ PyTorch 版本：", torch.__version__)
        print("✅ CUDA 是否可用：", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("✅ 当前 CUDA 设备名：", torch.cuda.get_device_name(0))
        else:
            print("⚠️ 没有检测到 CUDA GPU，PyTorch 将使用 CPU。")
    except ImportError:
        print("❌ 没有安装 PyTorch，请运行： pip install torch")


if __name__ == '__main__':
    check_environment()
