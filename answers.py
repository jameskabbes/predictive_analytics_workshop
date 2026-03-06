# sse = 0
# for point in points:
#     y_guess = line_function_guess(point.x)
#     sse += (point.y - y_guess) ** 2

# return sse


# m_grid, b_grid = np.meshgrid(m_samples, b_samples)


# contour = plt.contourf(m_grid, b_grid, sse_grid, levels=30, cmap='viridis')

# plt.colorbar(contour, label='SSE')
# plt.contour(m_grid, b_grid, sse_grid, levels=10, colors='white', alpha=0.4, linewidths=0.8)

# plt.xlabel('Slope (m)')
# plt.ylabel('Y-Intercept (b)')
# plt.title('SSE Surface')
# plt.grid(True, alpha=0.2)
# plt.legend()



    # n = len(points)

    # sum_x = sum([p.x for p in points])
    # sum_y = sum([p.y for p in points])

    # sum_xy = 0
    # sum_x2 = 0

    # for point in points:
    #     sum_xy += (point.x * point.y)
    #     sum_x2 += (point.x)**2

    # m_true = ((n*sum_xy)-(sum_x*sum_y))/((n*sum_x2)-sum_x**2)
    # b_true = (sum_y-(m_true*sum_x))/n

    # return BestFitLine(m=m_true, b=b_true)