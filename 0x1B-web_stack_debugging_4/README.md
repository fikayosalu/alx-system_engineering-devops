# Web Stack Debugging: Fixing Nginx Under Load

## Task Overview
This task involves debugging and optimizing an **Nginx web server** that is struggling to handle a high volume of concurrent requests. During a performance test using **ApacheBench (ab)**, we observed a significant number of failed requests, indicating that the server is **not configured properly** to handle heavy traffic.

Our goal is to **debug the web stack**, identify the bottleneck, and implement a solution to ensure all requests are served successfully.

## Tools Used
- **Nginx** – The web server we are debugging and optimizing.
- **ApacheBench (ab)** – A benchmarking tool used to simulate HTTP requests.
- **Puppet** – A configuration management tool to automate the fix.

## Identifying the Issue
The initial benchmark test was executed using:

```bash
ab -c 100 -n 2000 localhost/
```

### Observations:
- **943 failed requests** out of **2000 total requests**.
- **1057 non-2xx responses**, indicating that the server was not correctly handling many requests.
- **High concurrency issues**, likely due to default Nginx settings limiting the number of connections.

This suggests that Nginx is **not optimized** to efficiently handle high traffic, leading to dropped requests and performance degradation.

## The Fix
To resolve this, we created a **Puppet script (`0-the_sky_is_the_limit_not.pp`)** that:

1. **Increases worker processes and connections** to handle more concurrent requests.
2. **Optimizes buffer sizes** to prevent failures due to large requests.
3. **Adjusts timeouts** to prevent premature connection termination.
4. **Restarts Nginx** after applying the new settings.

## Applying the Fix
To apply the fix, run the following command:

```bash
puppet apply 0-the_sky_is_the_limit_not.pp
```

This modifies **`/etc/nginx/nginx.conf`** with optimized configurations and restarts the Nginx service.

## Verifying the Fix
After applying the fix, we rerun the benchmark test:

```bash
ab -c 100 -n 2000 localhost/
```

### Results After the Fix:
- **0 failed requests 🎉**
- **Higher request handling capacity**
- **Lower response time and improved performance**

## Conclusion
This task highlights the importance of **web stack debugging** when optimizing server performance. By adjusting **Nginx’s worker settings, buffers, and timeouts**, we successfully eliminated request failures and improved the server's ability to handle concurrent traffic.

Understanding how to **analyze logs**, use **benchmarking tools**, and apply **configuration management solutions** (like Puppet) is essential for debugging web stacks and maintaining optimal performance in production environments.

## Author
[Salu Oluwafikunayomi]


