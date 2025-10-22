import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle

# パラメータ設定
fps = 15
duration_sec = 60
total_frames = fps * duration_sec
num_gears = 10
rotation_ratio = 2

# 歯車の位置と半径
gear_positions = [(3, i * -1.2) for i in range(num_gears)]
gear_radius = 0.5

# 回転速度（回転/秒）
rotation_speeds = [1 / (rotation_ratio ** i) for i in range(num_gears)]

# 初期化
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_xlim(1.5, 5.5)
ax.set_ylim(-11.5, 1)
ax.set_aspect('equal')  # アスペクト比を等しくして真円にする
ax.axis('off')
# 余白を最小限にする
plt.tight_layout()
plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)

# 歯車の円とマーカー、テキスト
gear_circles = []
gear_markers = []
rotation_texts = []

for i, (x, y) in enumerate(gear_positions):
    # 円を描画
    circle = Circle((x, y), gear_radius, fill=False, linewidth=2, color='black')
    ax.add_patch(circle)
    gear_circles.append(circle)
    
    # 回転を示すマーカー（赤い点）
    marker, = ax.plot(x + gear_radius, y, 'ro', markersize=8)
    gear_markers.append(marker)
    
    # 回転数テキスト
    text = ax.text(x + gear_radius + 0.3, y, '', fontsize=10, color='black', va='center')
    rotation_texts.append(text)

# 経過時間テキスト
elapsed_text = ax.text(3, 1, '', fontsize=12, color='blue', ha='center')

# 回転角度（ラジアン）
rotation_angles = [0 for _ in range(num_gears)]

# 更新関数
def update(frame):
    elapsed_seconds = frame / fps
    elapsed_text.set_text(f'Elapsed time: {int(elapsed_seconds)} sec')
    
    # 各歯車の回転角度を更新
    for i in range(num_gears):
        rotation_angles[i] += rotation_speeds[i] * 2 * np.pi / fps
    
    # マーカーの位置を更新（円周上を回転）
    for i, (x, y) in enumerate(gear_positions):
        angle = rotation_angles[i]
        new_x = x + gear_radius * np.cos(angle)
        new_y = y + gear_radius * np.sin(angle)
        gear_markers[i].set_data([new_x], [new_y])
        
        # 回転数を表示
        rotations = rotation_angles[i] / (2 * np.pi)
        rotation_texts[i].set_text(f'{rotations:.2f} rotations')
    
    return gear_markers + rotation_texts + [elapsed_text]

# アニメーション作成
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000 / fps, blit=True)

# MP4として保存
ani.save('gear_rotation_2x_15fps_60sec.mp4', writer='ffmpeg', fps=fps)