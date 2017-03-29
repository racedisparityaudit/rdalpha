# == Schema Information
#
# Table name: taxonomy_levels
#
#  id          :integer          not null, primary key
#  level       :string
#  name        :string
#  parent_name :string
#  parent_id   :integer
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#  description :string
#  uri         :string
#  source      :string
#  display     :string
#  subtitle    :string
#

class TaxonomyLevel < ApplicationRecord
  has_many :taxonomy_levels, foreign_key: :parent_id
  belongs_to :taxonomy_level, foreign_key: :parent_id
  has_many :measure_averages
  HOMEPAGE_NAME = "homepage"

  def self.metrics
    all.select{ |t| t.metric_level?}
  end

  def self.homepage
    TaxonomyLevel.where(parent_id: nil).first
  end

  def self.topics
    TaxonomyLevel.where(parent_id: homepage.id)
  end

  def chart_tabs
    json_file["chart_tabs"]
  end

  def js_flag
    json_file["js_flag"]
  end

  def json_file
    return nil unless metric_level?
    @json_file ||= JSON.parse(File.read(json_uri))
  end

  def measure_explanation
    json_file["measure_explanation"]
  end
  def overall_summary
    json_file["overall_summary"]
  end

  def json_uri
    Rails.root.join("data/pages#{uri}/data.json")
  end

  def anchor
    name.split(" ").join("")
  end

  def breadcrumbs
    crumbs = [TaxonomyLevel.homepage]
    crumbs << top_level_parent if taxonomy_level
    crumbs << self if metric_level?
    crumbs
  end

  def link
    if uri == TaxonomyLevel.homepage.uri
      "/"
    elsif metric_level?
      "/#{ name }"
    else
      "/topics/#{top_level_parent.id}"
    end
  end

  def measures
    metric_level? ? self : taxonomy_levels.map(&:measures).flatten
  end

  def top_level_parent
    return self if topic_level?
    return taxonomy_level.top_level_parent
  end

  def topic_level?
    parent_name == "homepage"
  end

  def subtitle
    self[:subtitle] || "Description unavailable."
  end

  def national_average
    return "-" unless national
    display_encode(national)
  end

  def national
    return nil unless measure_averages.any?
    measure_averages.first.display_national
  end

  def group_average(group)
    return "-" unless group && number =  measure_average_for(group).try(:display_value)
    display_encode(number)
  end

  def display_name
    title.downcase.tap{ |n| n[0] = n.first.upcase }.gsub("&","and")
  end

  def breadcrumb_name
    name.downcase.tap{ |n| n[0] = n.first.upcase }.gsub("&","and")
  end

  def metric_level?
    taxonomy_levels.empty?
  end

  def parent_name
    taxonomy_level.name
  end

  def topic_overview
    case uri
    when "/education"
      ["Government departments, local authorities, schools, colleges and universities collect and report the following education data which includes ethnicity.",
        "This covers school and college results and progress, higher education, adult education, and where students go after leaving education."
      ]
    when "/work"
      ["Government departments, local authorities and Job Centres collect and report the following work data which includes ethnicity.",
        "This covers employment, pay and professions, benefits, workplace discrimination, Job Centres, and the public sector workforce diversity."]
    when "/housingandlivingstandards"
      ["Government departments and local authorities collect and report the following housing data which includes ethnicity.",
        "This covers home ownership and private renting, social housing, being homeless and losing your home, housing conditions and standard of living."]
    when "/health"
      ["Government departments, local authorities, hospitals, health trusts and organisations collect and report the following health data which includes ethnicity.",
        "This covers physical and mental health, preventing illness, quality of care, access to treatment, patient experiences, and patient outcomes."]
    when "/securityandjustice"
      ["Government departments, local authorities, police, border controls, law courts and prisons collect and report the following security and justice data which includes ethnicity.",
        "This covers justice, crimes, the police, and customs."]
    when "/privatelifeandcommunity"
      ["Government departments and local authorities collect and report the following data related to private life and communities which includes ethnicity.",
        "This covers home ownership and private renting, social housing, being homeless and losing your home, housing conditions and standard of living."]
    else
      ["Government departments, local authorities and related organisations collect and report the following data which includes ethnicity."]
    end
  end

  private

  def title
    name == HOMEPAGE_NAME ? "Entire public sector" : name
  end

  def measure_average_for(group)
    measure_averages.select{ |a|
      a.subgroup_name.split(" ").first.downcase == group.split(" ").first.downcase }.first
  end

  def display_encode(number_string)
    # TODO: awful it gets confused because of use of keyword
    if self[:display] == "percent" || self[:display].nil?
      (number_string.to_d * 100).round(1).to_s + " %"
    else
      number_string.to_d.round(2).to_s
    end
  end

end
