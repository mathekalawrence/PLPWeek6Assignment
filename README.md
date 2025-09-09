# PLPWeek6Assignment
**Features Implemented**
**Multiple URLs**

Users can paste multiple URLs separated by commas.

The program loops and fetches each image.

**Precautions for unknown sources**

Adds a custom User-Agent header.

Checks Content-Type header to ensure the response is actually an image and not otherwise

Prevent duplicate images

Uses SHA-256 hash of image contents to detect and skip duplicates.

Important HTTP headers checked

Content-Type: must start with image/ before saving.

User-Agent: respectful request header.

Ubuntu Principles

Respectful messages.

Emphasis on community and mindfulness.
