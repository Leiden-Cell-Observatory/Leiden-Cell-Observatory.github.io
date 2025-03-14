# High-Content Screening (HCS) Data

This guide covers importing and managing high-content screening data in OMERO.

## HCS Data Structure

OMERO supports the hierarchical organization of HCS data:
- Plate
  - Well
    - Field
      - Channel
        - Timepoint

## Import Considerations

### Metadata Requirements
- Plate layout information
- Well naming conventions
- Experimental conditions
- Treatment annotations

### File Organization
1. Maintain original plate structure
2. Keep metadata files with raw data
3. Document plate layouts
4. Preserve screen/plate relationships

## Best Practices

### Before Import
1. **Organize Data**
   - Group plates by screen
   - Maintain consistent naming
   - Document experimental conditions

2. **Prepare Metadata**
   - Create plate layouts
   - Document treatments
   - Note quality control metrics

### During Import
1. **Verify Plate Structure**
   - Check well detection
   - Confirm field count
   - Validate channel settings

2. **Add Annotations**
   - Screen information
   - Experimental conditions
   - Quality metrics

### After Import
1. **Validate Data**
   - Check plate layout
   - Verify well positions
   - Confirm metadata

2. **Organization**
   - Group related plates
   - Add screen-level annotations
   - Link to protocols