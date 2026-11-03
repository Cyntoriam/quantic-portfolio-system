CREATE TABLE projects (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500) NOT NULL,
    category VARCHAR(60) NOT NULL,
    technologies TEXT[] NOT NULL DEFAULT '{}',
    href TEXT,
    display_order INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT projects_title_not_blank CHECK (length(trim(title)) > 0),
    CONSTRAINT projects_description_not_blank CHECK (length(trim(description)) > 0),
    CONSTRAINT projects_category_not_blank CHECK (length(trim(category)) > 0)
);

CREATE INDEX projects_display_order_idx ON projects (display_order, id);

CREATE TABLE contact_messages (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'new',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT contact_messages_name_not_blank CHECK (length(trim(name)) > 0),
    CONSTRAINT contact_messages_email_not_blank CHECK (length(trim(email)) > 0),
    CONSTRAINT contact_messages_message_not_blank CHECK (length(trim(message)) > 0),
    CONSTRAINT contact_messages_status_valid CHECK (status IN ('new', 'read', 'archived'))
);

CREATE INDEX contact_messages_created_at_idx ON contact_messages (created_at DESC);

CREATE TABLE certifications (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    issuer VARCHAR(100) NOT NULL,
    score_details VARCHAR(100),
    description TEXT NOT NULL,
    badge_image_url VARCHAR(255),
    credential_url VARCHAR(255) UNIQUE
);

INSERT INTO certifications (
    name,
    issuer,
    score_details,
    description,
    badge_image_url,
    credential_url
)
VALUES (
    'AMD ROCm Certified Associate',
    'AMD',
    'Issuer: AMD',
    'Validated foundational knowledge of AMD accelerated computing and HPC application optimization using AMD ROCm™.',
    'https://images.credly.com/images/b565e2d0-df9c-42c4-bbaf-132a00cd36b9/image.png',
    'https://www.credly.com/badges/b565e2d0-df9c-42c4-bbaf-132a00cd36b9/public_url'
)
ON CONFLICT (credential_url) DO NOTHING;
