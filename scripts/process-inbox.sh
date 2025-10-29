#!/bin/bash

# Inbox Processing Script
# Processes inbox files and updates inbox.md

set -e

INBOX_DIR="/Users/simon/git/productivity-system/inbox"
INBOX_MD="/Users/simon/git/productivity-system/inbox.md"
PRACTICE_DIR="/Users/simon/git/productivity-system/personal/practice"
ARCHIVE_DIR="/Users/simon/git/productivity-system/archive"

echo "🔄 Processing inbox..."
echo ""

# Count files
TOTAL_FILES=$(find "$INBOX_DIR" -type f -name "*.md" | wc -l | tr -d ' ')
PRIO_FILES=$(find "$INBOX_DIR" -type f -name "*Prio*.md" -o -name "*PRIO*.md" -o -name "*priority*.md" | wc -l | tr -d ' ')

echo "📊 Inbox Status:"
echo "   Total files: $TOTAL_FILES"
echo "   Priority files: $PRIO_FILES"
echo ""

# Interactive processing
echo "🎯 Interactive Processing Mode"
echo ""

for file in "$INBOX_DIR"/*.md; do
    [ -f "$file" ] || continue

    filename=$(basename "$file")

    # Skip if already processed marker exists
    if [[ "$filename" == *"PROCESSED"* ]]; then
        continue
    fi

    echo "----------------------------------------"
    echo "📄 File: $filename"
    echo "📅 Date: $(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$file")"

    # Show file size
    filesize=$(stat -f "%z" "$file")
    echo "📦 Size: $filesize bytes"

    # Show first 10 lines of content if not empty
    if [ "$filesize" -gt 0 ]; then
        echo ""
        echo "📝 Preview:"
        head -10 "$file" | sed 's/^/   /'
        echo ""
    else
        echo "   (Empty file)"
        echo ""
    fi

    # Processing options
    echo "Choose action:"
    echo "  1) Archive (move to archive/)"
    echo "  2) Move to practice (personal/practice/)"
    echo "  3) Delete"
    echo "  4) Skip (process later)"
    echo "  5) Open in editor"
    echo "  q) Quit processing"
    echo ""

    read -p "Action [1-5/q]: " action

    case $action in
        1)
            mv "$file" "$ARCHIVE_DIR/"
            echo "✅ Archived: $filename"
            ;;
        2)
            mv "$file" "$PRACTICE_DIR/"
            echo "✅ Moved to practice: $filename"
            ;;
        3)
            rm "$file"
            echo "🗑️  Deleted: $filename"
            ;;
        4)
            echo "⏭️  Skipped: $filename"
            ;;
        5)
            ${EDITOR:-nano} "$file"
            echo "📝 Edited: $filename (re-evaluating...)"
            # Re-prompt after edit
            continue
            ;;
        q)
            echo ""
            echo "👋 Exiting inbox processing..."
            break
            ;;
        *)
            echo "⏭️  Invalid choice, skipping: $filename"
            ;;
    esac

    echo ""
done

echo ""
echo "----------------------------------------"
echo "✅ Inbox processing complete!"
echo ""

# Update statistics
REMAINING=$(find "$INBOX_DIR" -type f -name "*.md" | wc -l | tr -d ' ')
echo "📊 Final Status:"
echo "   Remaining items: $REMAINING"
echo ""

# Generate inbox.md summary
echo "📝 Updating inbox.md..."

cat > "$INBOX_MD" << 'HEADER'
# Inbox Processing Queue

> **Last Updated:** $(date +%Y-%m-%d)
> **Total Items:** REMAINING_COUNT

---

## 🔴 PRIORITY ITEMS (Process First!)

HEADER

# Find and list priority items
find "$INBOX_DIR" -type f \( -name "*Prio*" -o -name "*PRIO*" -o -name "*priority*" \) | while read -r pfile; do
    pfilename=$(basename "$pfile")
    pdate=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$pfile")

    echo "### $pfilename" >> "$INBOX_MD"
    echo "**Date:** $pdate" >> "$INBOX_MD"

    if [ -s "$pfile" ]; then
        echo "**Content:**" >> "$INBOX_MD"
        echo '```' >> "$INBOX_MD"
        head -20 "$pfile" >> "$INBOX_MD"
        echo '```' >> "$INBOX_MD"
    else
        echo "**Status:** Empty file" >> "$INBOX_MD"
    fi

    echo "" >> "$INBOX_MD"
    echo "---" >> "$INBOX_MD"
    echo "" >> "$INBOX_MD"
done

echo "" >> "$INBOX_MD"
echo "## 📥 Standard Queue" >> "$INBOX_MD"
echo "" >> "$INBOX_MD"

# List non-priority items
counter=1
find "$INBOX_DIR" -type f -name "*.md" ! -name "*Prio*" ! -name "*PRIO*" ! -name "*priority*" | while read -r nfile; do
    nfilename=$(basename "$nfile")
    ndate=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$nfile")

    echo "### $counter. $nfilename" >> "$INBOX_MD"
    echo "**Date:** $ndate" >> "$INBOX_MD"

    if [ -s "$nfile" ]; then
        echo "**Content:**" >> "$INBOX_MD"
        echo '```' >> "$INBOX_MD"
        head -10 "$nfile" >> "$INBOX_MD"
        echo '```' >> "$INBOX_MD"
    else
        echo "**Status:** Empty file" >> "$INBOX_MD"
    fi

    echo "" >> "$INBOX_MD"
    echo "---" >> "$INBOX_MD"
    echo "" >> "$INBOX_MD"

    ((counter++))
done

# Update counts in header
sed -i '' "s/REMAINING_COUNT/$REMAINING/" "$INBOX_MD"
sed -i '' "s/\$(date +%Y-%m-%d)/$(date +%Y-%m-%d)/" "$INBOX_MD"

echo "✅ inbox.md updated!"
echo ""
echo "🎉 All done! Inbox status:"
echo "   Items remaining: $REMAINING"
[ "$REMAINING" -eq 0 ] && echo "   🎊 INBOX ZERO ACHIEVED! 🎊"
echo ""
