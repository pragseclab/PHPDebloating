<?php

/* privileges/privileges_summary.twig */
class __TwigTemplate_4d3c125d3a5a8adc76df3a94d959a05db97b8b05aa85bfe01b391dc53a61565c extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<form class=\"submenu-item\" action=\"server_privileges.php\" id=\"";
        echo twig_escape_filter($this->env, (isset($context["form_id"]) ? $context["form_id"] : null), "html", null, true);
        echo "\" method=\"post\">
    ";
        // line 2
        echo PhpMyAdmin\Url::getHiddenInputs();
        echo "
    <input type=\"hidden\" name=\"username\" value=\"";
        // line 3
        echo twig_escape_filter($this->env, (isset($context["username"]) ? $context["username"] : null), "html", null, true);
        echo "\" />
    <input type=\"hidden\" name=\"hostname\" value=\"";
        // line 4
        echo twig_escape_filter($this->env, (isset($context["hostname"]) ? $context["hostname"] : null), "html", null, true);
        echo "\" />

    <fieldset>
        <legend data-submenu-label=\"";
        // line 7
        echo twig_escape_filter($this->env, (isset($context["sub_menu_label"]) ? $context["sub_menu_label"] : null), "html", null, true);
        echo "\">
            ";
        // line 8
        echo twig_escape_filter($this->env, (isset($context["legend"]) ? $context["legend"] : null), "html", null, true);
        echo "
        </legend>

        <table class=\"data\">
            <thead>
                <tr>
                    <th>";
        // line 14
        echo twig_escape_filter($this->env, (isset($context["type_label"]) ? $context["type_label"] : null), "html", null, true);
        echo "</th>
                    <th>";
        // line 15
        echo _gettext("Privileges");
        echo "</th>
                    <th>";
        // line 16
        echo _gettext("Grant");
        echo "</th>
                    ";
        // line 17
        if (((isset($context["type"]) ? $context["type"] : null) == "database")) {
            // line 18
            echo "                        <th>";
            echo _gettext("Table-specific privileges");
            echo "</th>
                    ";
        } elseif ((        // line 19
(isset($context["type"]) ? $context["type"] : null) == "table")) {
            // line 20
            echo "                        <th>";
            echo _gettext("Column-specific privileges");
            echo "</th>
                    ";
        }
        // line 22
        echo "                    <th colspan=\"2\">";
        echo _gettext("Action");
        echo "</th>
                </tr>
            </thead>

            <tbody>
                ";
        // line 27
        if ((twig_length_filter($this->env, (isset($context["privileges"]) ? $context["privileges"] : null)) == 0)) {
            // line 28
            echo "                    ";
            $context["colspan"] = ((((isset($context["type"]) ? $context["type"] : null) == "database")) ? (7) : (((((isset($context["type"]) ? $context["type"] : null) == "table")) ? (6) : (5))));
            // line 29
            echo "                    <tr>
                        <td colspan=\"";
            // line 30
            echo twig_escape_filter($this->env, (isset($context["colspan"]) ? $context["colspan"] : null), "html", null, true);
            echo "\"><center><em>";
            echo _gettext("None");
            echo "</em></center></td>
                    </tr>
                ";
        } else {
            // line 33
            echo "                    ";
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable((isset($context["privileges"]) ? $context["privileges"] : null));
            foreach ($context['_seq'] as $context["_key"] => $context["privilege"]) {
                // line 34
                echo "                        ";
                $this->loadTemplate("privileges/privileges_summary_row.twig", "privileges/privileges_summary.twig", 34)->display(twig_array_merge(                // line 35
$context["privilege"], array("type" => (isset($context["type"]) ? $context["type"] : null))));
                // line 37
                echo "                    ";
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_iterated'], $context['_key'], $context['privilege'], $context['_parent'], $context['loop']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 38
            echo "                ";
        }
        // line 39
        echo "            </tbody>
        </table>

        ";
        // line 42
        if (((isset($context["type"]) ? $context["type"] : null) == "database")) {
            // line 43
            echo "            ";
            $this->loadTemplate("privileges/add_privileges_database.twig", "privileges/privileges_summary.twig", 43)->display(array("databases" =>             // line 44
(isset($context["databases"]) ? $context["databases"] : null)));
            // line 46
            echo "        ";
        } elseif (((isset($context["type"]) ? $context["type"] : null) == "table")) {
            // line 47
            echo "            ";
            $this->loadTemplate("privileges/add_privileges_table.twig", "privileges/privileges_summary.twig", 47)->display(array("database" =>             // line 48
(isset($context["database"]) ? $context["database"] : null), "tables" =>             // line 49
(isset($context["tables"]) ? $context["tables"] : null)));
            // line 51
            echo "        ";
        } else {
            // line 52
            echo "            ";
            $this->loadTemplate("privileges/add_privileges_routine.twig", "privileges/privileges_summary.twig", 52)->display(array("database" =>             // line 53
(isset($context["database"]) ? $context["database"] : null), "routines" =>             // line 54
(isset($context["routines"]) ? $context["routines"] : null)));
            // line 56
            echo "        ";
        }
        // line 57
        echo "    </fieldset>

    <fieldset class=\"tblFooters\">
        <input type=\"submit\" value=\"";
        // line 60
        echo _gettext("Go");
        echo "\" />
    </fieldset>
</form>
";
    }

    public function getTemplateName()
    {
        return "privileges/privileges_summary.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  156 => 60,  151 => 57,  148 => 56,  146 => 54,  145 => 53,  143 => 52,  140 => 51,  138 => 49,  137 => 48,  135 => 47,  132 => 46,  130 => 44,  128 => 43,  126 => 42,  121 => 39,  118 => 38,  112 => 37,  110 => 35,  108 => 34,  103 => 33,  95 => 30,  92 => 29,  89 => 28,  87 => 27,  78 => 22,  72 => 20,  70 => 19,  65 => 18,  63 => 17,  59 => 16,  55 => 15,  51 => 14,  42 => 8,  38 => 7,  32 => 4,  28 => 3,  24 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "privileges/privileges_summary.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/privileges/privileges_summary.twig");
    }
}
